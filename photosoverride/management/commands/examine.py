import argparse
import shlex
from collections import defaultdict
from typing import Dict, List, Optional, Set

from photosoverride.management.command import LibraryCommand
from photosoverride.models import (
    AdditionalAssetAttributes,
    Asset,
    AssetKeywords,
    Keyword,
)


class Command(LibraryCommand):
    def add_arguments(self, parser: argparse.ArgumentParser):
        super().add_arguments(parser)
        parser.add_argument(
            "--duplicate-keyword", help="Keyword to add to duplicate pictures."
        )
        parser.add_argument(
            "--original-keyword",
            help="Keyword to add to the first of duplicate pictures.",
        )
        parser.add_argument(
            "--missing-keyword", help="Keyword to add to missing pictures."
        )
        parser.add_argument(
            "--clean-keywords",
            help="Remove keywords from all pictures.",
            default=False,
            action="store_true",
        )
        parser.add_argument(
            "--small-size",
            help="Max size of small pictures (in bytes).",
            default=100 * 1000,
            type=int,
        )
        parser.add_argument(
            "--large-size",
            help="Min size of large pictures (in bytes).",
            default=50 * 1000 * 1000,
            type=int,
        )
        parser.add_argument("--small-keyword", help="Keyword to add to small pictures.")
        parser.add_argument("--large-keyword", help="Keyword to add to large pictures.")
        parser.add_argument(
            "--no-md5",
            help="Do not use md5 to compare pictures, only EXIF timestamp.",
            default=True,
            action="store_false",
            dest="compare_md5",
        )

    @staticmethod
    def get_keyword(value: Optional[str]) -> Optional[Keyword]:
        if not value:
            return None
        return Keyword.objects.get(title=value)

    def handle(self, *args, **options):
        missing_keyword = self.get_keyword(options["missing_keyword"])
        duplicate_keyword = self.get_keyword(options["duplicate_keyword"])
        original_keyword = self.get_keyword(options["original_keyword"])
        large_keyword = self.get_keyword(options["large_keyword"])
        large_size = options["large_size"]
        small_keyword = self.get_keyword(options["small_keyword"])
        small_size = options["small_size"]
        clean_keywords: bool = options["clean_keywords"]
        use_md5: bool = options["compare_md5"]

        keywords_existing: Dict[int, Set[int]] = defaultdict(lambda: set())
        duplicates: Dict[str, List[AdditionalAssetAttributes]] = defaultdict(lambda: [])
        for keyword in (missing_keyword, large_keyword, small_keyword):
            if not keyword:
                continue
            qs = AssetKeywords.objects.filter(z_38keywords_id=keyword.pk)
            if clean_keywords:
                qs.delete()
            else:
                keywords_existing[keyword.pk] |= set(
                    qs.values_list("z_1assetattributes_id", flat=True)
                )

        keywords_to_add = []
        for ext in AdditionalAssetAttributes.objects.all().select_related("asset"):
            if ext.exif_timestamp_string:
                duplicates[ext.exif_timestamp_string].append(ext)
            if ext.original_filesize and use_md5:
                duplicates[str(ext.original_filesize)].append(ext)
            if (
                small_keyword
                and ext.original_filesize < small_size
                and ext.pk not in keywords_existing[small_keyword.pk]
            ):
                self.stderr.write(
                    self.style.WARNING("Small picture: %s (%d bytes)")
                    % (ext.asset.picture_path, ext.original_filesize)
                )
                keywords_to_add.append(
                    AssetKeywords(
                        z_38keywords_id=small_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
                keywords_existing[small_keyword.pk].add(ext.pk)
            if (
                large_keyword
                and ext.original_filesize > large_size
                and ext.pk not in keywords_existing[large_keyword.pk]
            ):
                self.stdout.write(
                    self.style.WARNING("Large picture: %s (%d bytes)")
                    % (ext.asset.picture_path, ext.original_filesize)
                )
                keywords_to_add.append(
                    AssetKeywords(
                        z_38keywords_id=large_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
                keywords_existing[large_keyword.pk].add(ext.pk)

            if (
                missing_keyword
                and not ext.asset.picture_path.exists()
                and ext.pk not in keywords_existing[missing_keyword.pk]
            ):
                self.stderr.write("Missing file: %s" % ext.asset.picture_path)
                keywords_to_add.append(
                    AssetKeywords(
                        z_38keywords_id=missing_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
                keywords_existing[missing_keyword.pk].add(ext.pk)
        AssetKeywords.objects.bulk_create(keywords_to_add)
        self.find_duplicates(
            original_keyword,
            duplicate_keyword,
            duplicates,
            clean_keywords=clean_keywords,
            use_md5=use_md5,
        )

    def find_duplicates(
        self,
        original_keyword: Optional[Keyword],
        duplicate_keyword: Optional[Keyword],
        duplicates: Dict[str, List[AdditionalAssetAttributes]],
        clean_keywords: bool = False,
        use_md5: bool = False,
    ):
        values = []
        duplicate_existing = set()
        if original_keyword:
            values.append(original_keyword.pk)
        if duplicate_keyword:
            values.append(duplicate_keyword.pk)
        if clean_keywords:
            AssetKeywords.objects.filter(z_38keywords_id__in=values).delete()
        else:
            qs = AssetKeywords.objects.filter(z_38keywords_id__in=values)
            duplicate_existing = set(qs.values_list("z_1assetattributes_id", flat=True))
        if use_md5:
            actual_candidates_lists: List[List[Asset]] = []
            for key, candidates_list in duplicates.items():
                if len(candidates_list) > 1:
                    actual_candidates_lists.append([x.asset for x in candidates_list])
            actual_duplicates_by_shasum = defaultdict(lambda: [])
            for candidates_list in actual_candidates_lists:
                for candidate in candidates_list:
                    if candidate.picture_path.exists():
                        actual_duplicates_by_shasum[candidate.shasum].append(candidate)
        else:
            actual_duplicates_by_shasum = {
                x: [y.asset for y in z] for (x, z) in duplicates.items()
            }
        duplicate_to_create = []
        for actual_duplicates in actual_duplicates_by_shasum.values():
            if len(actual_duplicates) == 1:
                continue
            actual_duplicates.sort(key=lambda x: x.z_pk)
            dup: Asset = actual_duplicates[0]
            msg = " ".join(
                [shlex.quote(str(x.picture_path.absolute())) for x in actual_duplicates]
            )
            self.stdout.write(self.style.SUCCESS(msg))
            obj = dup.additionalattributes_id
            if obj not in duplicate_existing:
                duplicate_existing.add(obj)
                if original_keyword:
                    duplicate_to_create.append(
                        AssetKeywords(
                            z_38keywords_id=original_keyword.pk,
                            z_1assetattributes_id=obj,
                        )
                    )
            if not duplicate_keyword:
                continue
            for dup in actual_duplicates[1:]:
                obj_id = dup.additionalattributes_id
                if obj_id not in duplicate_existing:
                    duplicate_existing.add(obj_id)
                    duplicate_to_create.append(
                        AssetKeywords(
                            z_38keywords_id=duplicate_keyword.pk,
                            z_1assetattributes_id=obj_id,
                        )
                    )
        AssetKeywords.objects.bulk_create(duplicate_to_create)
