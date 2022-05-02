#!/usr/bin/env python3


from importlib import import_module as inkoke
from pathlib import Path as libPath
from os import getcwd, path, chdir


project_name = "ProjectDesignBuilder"
__version__ = "0.0.2"
__release__ = "0.0.0"


def assistant(request = None, registration = None):
    """In administration, the Administrator further collaborates with other
    deligates, managers, and directors.  These associates provide guidance,
    directives, assignments and additional introductions.  Welcome to
    ProjectDesignBuilder!"""

    # Locate the project directory and navigate to it.
    project_path = path.dirname(path.abspath(__file__.replace('./', '')))\
        .split(project_name)[0] + project_name
    if path.abspath(getcwd()) is not project_path:
        chdir(project_path)

    # Find the administration office.
    filepath = sorted(libPath('.').glob('**/' + request + '.py'))
    request = str(filepath).split('\'')[1]
    administrator = (
        f".{request.rsplit('/', 1)[1].strip('.py').replace('/', '.')}")
    office = request.rsplit('/', 1)[0].replace('/', '.')

    # Now go into the office and request registration.
    request = inkoke(administrator, office)
    register = getattr(request, registration)()

    # Import directors
    from Administrator import orientation
    from ProjectCoordinator import evaluate_arguments

    # Okay, you are registered, now goto orientation.
    orientation(register)
    # Now go check in with the ProjectCoordinator for evaluation.
    evaluate_arguments(register)

    return register


def main():
    """Greetings!  This is the main() entrance to ProjectDesignBuilder.
    The assistant() will guide you to the Administration office for
    registration."""

    # Go with the assistant to get registered.
    register = assistant('Administrator', 'registration')

    return register


# Proceed through the main() entrance.
if __name__ == "__main__":
    main()
