"""Allow the --library argument."""
from argparse import ArgumentParser

from django.core.management import BaseCommand

from photosoverride.run import populate_parser


class ConfigMixin:
    """Allow the --library argument."""

    def add_arguments(self: BaseCommand, parser: ArgumentParser):
        """Override the default method to allow --library argument."""
        populate_parser(parser)
        # noinspection PyUnresolvedReferences
        super().add_arguments(parser)
