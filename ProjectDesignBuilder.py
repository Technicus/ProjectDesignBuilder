#!/usr/bin/env python3
# ProjectDesignBuilder.py
# 2022.04.20.21.57

from importlib import import_module as introduce
from pathlib import Path as libPath


project_name = "ProjectDesignBuilder"
__version__ = "0.0.2"
__release__ = "0.0.0"


def assistant(Administrator = 'Administrator', assitant = 'assitant',):
    """Assistant administrator will direct you to the administration office,
    there you will be introduced with the Administrator.py module.  The
    assistant further collaborates with other deligates, managers, and
    directors.  These associates provide guidance, directives, assignments and
    additional introductions.  Welcome to ProjectDesignBuilder!"""
    filepath = sorted(libPath('.').glob('**/' + Administrator +'.py'))
    Administrator = str(filepath).split('\'')[1]
    main = f".{Administrator.rsplit('/', 1)[1].strip('.py').replace('/', '.')}"
    admin_office = Administrator.rsplit('/', 1)[0].replace('/', '.')
    asststant = introduce(main, admin_office)
    return getattr(asststant, assitant)()


def main():
    """Greetings!  This is the main() entrance for ProjectDesignBuilder.  The
    assistant() will introduced you to the Administrator in the administration
    office."""
    assistant()
    return None


# Proceed through the main() entrance.
if __name__ == "__main__":
    main()
