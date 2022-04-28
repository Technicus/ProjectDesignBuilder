#!/usr/bin/env python3
# ProjectDesignBuilder.py
# 2022.04.20.21.57

from importlib import import_module as inkoke
from pathlib import Path as libPath
from os import getcwd, path, chdir


project_name = "ProjectDesignBuilder"
__version__ = "0.0.2"
__release__ = "0.0.0"


def assistant(module = None, function = None):
    """In administration, the Administrator further collaborates with other
    deligates, managers, and directors.  These associates provide guidance,
    directives, assignments and additional introductions.  Welcome to
    ProjectDesignBuilder!"""
    # Change the current working directory to the project directory.
    project_path = path.dirname(path.abspath(__file__.replace('./', '')))\
        .split(project_name)[0] + project_name
    if path.abspath(getcwd()) is not project_path:
        chdir(project_path)
    # Find the administration office.
    filepath = sorted(libPath('.').glob('**/' + module + '.py'))
    module = str(filepath).split('\'')[1]
    module_name = f".{module.rsplit('/', 1)[1].strip('.py').replace('/', '.')}"
    module_path = module.rsplit('/', 1)[0].replace('/', '.')
    module = inkoke(module_name, module_path)
    # Now the assistant will tak you to orientation.
    return getattr(module, function)()


def main():
    """Greetings!  This is the main() entrance to ProjectDesignBuilder.
    assistant() will introduce you to the Administration office for
    registration."""
    assistant('Administrator', 'registration')
    return None


# Proceed through the main() entrance.
if __name__ == "__main__":
    main()
