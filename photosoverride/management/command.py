"""Allow the --library argument."""
from argparse import ArgumentParser

from django.core.management import BaseCommand

from photosoverride.run import populate_parser


class LibraryCommand(BaseCommand):
    """Allow the --library argument."""

    def handle(self, *args, **options):
        raise NotImplementedError

    def add_arguments(self, parser: ArgumentParser):
        """Override the default method to allow --library argument."""
        populate_parser(parser)
        # noinspection PyUnresolvedReferences
        super().add_arguments(parser)
