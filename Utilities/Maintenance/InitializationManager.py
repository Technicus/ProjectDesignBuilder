#!/bin/python
# InitializationManager.py
# 2022.04.20.21.57


# from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv

# from inspect import currentframe, getframeinfo, trace
# from ast import literal_eval
# from linecache import getline
from importlib import import_module as invoke
from inspect import currentframe  # , getframeinfo, trace


project_name = invoke("ProjectDesignBuilder", "").project_name
__version__ = invoke("ProjectDesignBuilder", "").__version__
__release__ = invoke("ProjectDesignBuilder", "").__release__


def initalize(
        project_path = invoke('.UtilityManager', 'Utilities.Maintenance').set_project_directory(),
        directory_omit = ['.git', '__', 'html'],
        file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']):
    """Set initial state of project start conditions.
    Establish the project directory, and return the registry."""
    # Establish working path.
    #project_path = parse_directory_path(False)
    # Identify path to 'RegistryManager.py'.
    #print(f"\ngetcwd():\n  {getcwd()}\n")

    # Find the file then distill it down to the relative path from projec path.
    # with that then call it with the import module.  Perhaps it would be
    # more direct if that was part of the search function.

    #registry_manager_path = find_file(project_path, 'RegistryManager.py', True)
    #print(f">>registry_manager_path\n  {registry_manager_path}\n")
    #print(f">>>> registry_manager_path:\n     {registry_manager_path}\n")
    print(f"project_root:\n  {project_path}\n")
    print(f"project_name:\n  {project_name}\n")
    print(f"directory_omit:\n  {directory_omit}\n")
    print(f"file_register_types:\n  {file_register_types}")

    # Create a registry.
    #registry = invoke('.RegistryManager', '.Utilities.Maintenance').Registry()
    #project_path = invoke('.UtilityManager',   'Utilities.Maintenance').set_project_directory(),
    registry = invoke('.RegistryManager', 'Utilities.Maintenance').Registry(
            str(project_path),
            project_name,
            directory_omit,
            file_register_types)


    return registry
