"""Management script to remove useless commands."""
import argparse
import os
import pathlib
import sys
from functools import lru_cache

REMOVED_DJANGO_COMMANDS = {
    "check": False,
    "compilemessages": False,
    "createcachetable": False,
    "diffsettings": False,
    "dumpdata": False,
    "flush": False,
    "loaddata": False,
    "makemessages": False,
    "makemigrations": False,
    "runserver": False,
    "sendtestemail": False,
    "sqlflush": False,
    "sqlmigrate": False,
    "sqlsequencereset": False,
    "squashmigrations": False,
    "startapp": False,
    "startproject": False,
    "test": True,
    "testserver": False,
    "showmigrations": False,
    "migrate": False,
}


def populate_parser(parser: argparse.ArgumentParser):
    """Add the --library argument."""
    parser.add_argument(
        "--library",
        default=pathlib.Path("~/Pictures/Photos Library.photoslibrary"),
        type=pathlib.Path,
    )


def main():
    """Run administrative tasks."""
    parser = argparse.ArgumentParser(add_help=False)
    populate_parser(parser)
    args, __ = parser.parse_known_args(sys.argv)
    library: pathlib.Path = args.library
    os.environ["PHOTOS_LIBRARY"] = str(library.expanduser().resolve())
    os.environ["DJANGO_SETTINGS_MODULE"] = "photosoverride.settings"
    import django.core.management as m
    from django.apps import apps
    from django.conf import settings

    def cleaned_get_commands():
        commands = {name: "django.core" for name in m.find_commands(m.__path__[0])}
        if not settings.configured:
            return commands

        for app_config in reversed(list(apps.get_app_configs())):
            path = os.path.join(app_config.path, "management")
            commands.update({name: app_config.name for name in m.find_commands(path)})
        for name, dev_mode in REMOVED_DJANGO_COMMANDS.items():
            if name in commands and not dev_mode:
                del commands[name]
        return commands

    setattr(m, "get_commands", lru_cache(cleaned_get_commands))
    m.execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
