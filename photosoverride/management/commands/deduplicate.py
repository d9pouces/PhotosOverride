import argparse
from collections import defaultdict
from typing import Dict, List

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
            "--original-keyword", help="Keyword to add to original pictures."
        )
        parser.add_argument(
            "--missing-keyword", help="Keyword to add to missing pictures."
        )

    def handle(self, *args, **options):
        missing_keyword = Zkeyword.objects.get(title=options["missing_keyword"])
        duplicate_keyword = Zkeyword.objects.get(title=options["duplicate_keyword"])
        original_keyword = Zkeyword.objects.get(title=options["original_keyword"])
        duplicates: Dict[str, List[Zadditionalassetattributes]] = defaultdict(
            lambda: []
        )
        Z1Keywords.objects.filter(
            z_38keywords_id__in=[original_keyword.pk, duplicate_keyword.pk]
        ).delete()
        missing_existing = set(
            Z1Keywords.objects.filter(z_38keywords_id=missing_keyword.pk).values_list(
                "z_1assetattributes_id", flat=True
            )
        )
        duplicate_existing = set(
            Z1Keywords.objects.filter(
                z_38keywords_id__in=[original_keyword.pk, duplicate_keyword.pk]
            ).values_list("z_1assetattributes_id", flat=True)
        )
        missing_to_create = []
        for ext in Zadditionalassetattributes.objects.all().select_related("asset"):
            if ext.exif_timestamp_string:
                duplicates[ext.exif_timestamp_string].append(ext)
            if ext.original_filesize:
                duplicates[str(ext.original_filesize)].append(ext)
            if not ext.asset.picture_path.exists() and ext.pk not in missing_existing:
                missing_to_create.append(
                    Z1Keywords(
                        z_38keywords_id=missing_keyword.pk, z_1assetattributes_id=ext.pk
                    )
                )
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
            if dup.additionalattributes_id not in duplicate_existing:
                duplicate_existing.add(dup.additionalattributes_id)
                duplicate_to_create.append(
                    Z1Keywords(
                        z_38keywords_id=original_keyword.pk,
                        z_1assetattributes_id=dup.additionalattributes_id,
                    )
                )
            print("%s: %s copies" % (dup.picture_path, len(actual_duplicates)))

            for dup in actual_duplicates[1:]:
                if dup.additionalattributes_id not in duplicate_existing:
                    duplicate_existing.add(dup.additionalattributes_id)
                    duplicate_to_create.append(
                        Z1Keywords(
                            z_38keywords_id=duplicate_keyword.pk,
                            z_1assetattributes_id=dup.additionalattributes_id,
                        )
                    )
        Z1Keywords.objects.bulk_create(duplicate_to_create)
        Z1Keywords.objects.bulk_create(missing_to_create)
