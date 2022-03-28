import argparse
from collections import defaultdict
from typing import Dict, List, Optional, Set

from photosoverride.management.command import LibraryCommand
from photosoverride.models import (
    Z1Keywords,
    Zadditionalassetattributes,
    Zasset,
    Zkeyword,
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

    @staticmethod
    def get_keyword(value: Optional[str]) -> Optional[Zkeyword]:
        if not value:
            return None
        return Zkeyword.objects.get(title=value)

    def handle(self, *args, **options):
        missing_keyword = self.get_keyword(options["missing_keyword"])
        duplicate_keyword = self.get_keyword(options["duplicate_keyword"])
        original_keyword = self.get_keyword(options["original_keyword"])
        large_keyword = self.get_keyword(options["large_keyword"])
        large_size = options["large_size"]
        small_keyword = self.get_keyword(options["small_keyword"])
        small_size = options["small_size"]

        keywords_existing: Dict[int, Set[int]] = defaultdict(lambda: set())
        duplicates: Dict[str, List[Zadditionalassetattributes]] = defaultdict(
            lambda: []
        )
        for keyword in (missing_keyword, large_keyword, small_keyword):
            if keyword:
                qs = Z1Keywords.objects.filter(z_38keywords_id=keyword.pk)
                keywords_existing[keyword.pk] |= set(
                    qs.values_list("z_1assetattributes_id", flat=True)
                )

        keywords_to_add = []
        for ext in Zadditionalassetattributes.objects.all().select_related("asset"):
            if ext.exif_timestamp_string:
                duplicates[ext.exif_timestamp_string].append(ext)
            if ext.original_filesize:
                duplicates[str(ext.original_filesize)].append(ext)
            if (
                small_keyword
                and ext.original_filesize < small_size
                and ext.pk not in keywords_existing[small_keyword.pk]
            ):
                self.stderr.write(
                    "Small picture: %s (%d bytes)"
                    % (ext.asset.picture_path, ext.original_filesize)
                )
                keywords_to_add.append(
                    Z1Keywords(
                        z_38keywords_id=small_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
                keywords_existing[small_keyword.pk].add(ext.pk)
            if (
                large_keyword
                and ext.original_filesize > large_size
                and ext.pk not in keywords_existing[large_keyword.pk]
            ):
                self.stderr.write(
                    "Small picture: %s (%d bytes)"
                    % (ext.asset.picture_path, ext.original_filesize)
                )
                keywords_to_add.append(
                    Z1Keywords(
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
                    Z1Keywords(
                        z_38keywords_id=missing_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
                keywords_existing[missing_keyword.pk].add(ext.pk)
        Z1Keywords.objects.bulk_create(keywords_to_add)

        self.find_duplicates(original_keyword, duplicate_keyword, duplicates)

    def find_duplicates(
        self,
        original_keyword: Optional[Zkeyword],
        duplicate_keyword: Optional[Zkeyword],
        duplicates: Dict[str, List[Zadditionalassetattributes]],
    ):
        if original_keyword and duplicate_keyword:
            values = [original_keyword.pk, duplicate_keyword.pk]
            Z1Keywords.objects.filter(z_38keywords_id__in=values).delete()
        elif original_keyword:
            Z1Keywords.objects.filter(z_38keywords_id=original_keyword.pk).delete()
        elif duplicate_keyword:
            Z1Keywords.objects.filter(z_38keywords_id=duplicate_keyword.pk).delete()
        duplicate_existing = set()
        actual_candidates_lists: List[List[Zasset]] = []
        for key, candidates_list in duplicates.items():
            if len(candidates_list) > 1:
                actual_candidates_lists.append([x.asset for x in candidates_list])
        actual_duplicates_by_shasum = defaultdict(lambda: [])
        for candidates_list in actual_candidates_lists:
            for candidate in candidates_list:
                if candidate.picture_path.exists():
                    actual_duplicates_by_shasum[candidate.shasum].append(candidate)
        duplicate_to_create = []
        for actual_duplicates in actual_duplicates_by_shasum.values():
            if len(actual_duplicates) == 1:
                continue
            actual_duplicates.sort(key=lambda x: x.z_pk)
            dup: Zasset = actual_duplicates[0]
            msg = "%s: %s copies" % (dup.picture_path, len(actual_duplicates))
            self.stdout.write(self.style.SUCCESS(msg))
            obj = dup.additionalattributes_id
            if obj not in duplicate_existing:
                duplicate_existing.add(obj)
                if original_keyword:
                    duplicate_to_create.append(
                        Z1Keywords(
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
                        Z1Keywords(
                            z_38keywords_id=duplicate_keyword.pk,
                            z_1assetattributes_id=obj_id,
                        )
                    )
        Z1Keywords.objects.bulk_create(duplicate_to_create)
