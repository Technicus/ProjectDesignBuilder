#!/bin/python
# InitializationManager.py


from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from inspect import currentframe, getframeinfo, trace
from ast import literal_eval
from linecache import getline
#from importlib import import_module
import importlib


project_name = 'ProjectDesignBuilder'


def parse_directory_path(project_root = 'file_path', parse_file = __file__):
    """Formerly known as set_project_directory(). A utility function to find
    the path of current file, and change the current working directory from
    that of the execution path to the current file path.  It takes one
    argument and returns a ptath variation.  It has no error handler."""
    if project_root == 'file_path':
        return path.dirname(path.abspath(parse_file.replace('./', '')))
    if project_root == 'project_path':
        return path.dirname(path.abspath(parse_file.replace('./', ''))).split(project_name)[0] + project_name
    if project_root == 'relative_path':
        return parse_directory_path('file_path').replace(parse_directory_path('project_path') + '/', './')
    if project_root == 'module_path':
        return parse_directory_path('file_path').replace(parse_directory_path('project_path') + '/', '.').replace('/', '.')


def set_project_directory():
    """This function was extracted from parse_directory_path.  It changes
    the current working directory to the project directory."""
    if path.abspath(getcwd()) is not parse_directory_path('file_path'):
        chdir(parse_directory_path('file_path'))
    return None


def find_file(search_path = None, filename = None, module_path = False):
    """Search through a given path for a specified file.
    :param filename:
    :type string:
    :param search_path:
    :type string:
    :return found_file:
    :rtype string:"""

    for root, dirs, files in walk(search_path):
        found_file = ''
        for name in files:
            if name == filename:
                found_file = path.join(root, name)
                if module_path:
                    found_file_base = found_file.rsplit('/', 1)[1].split('.')[0]
                    #found_file = parse_directory_path('module_path', found_file) + '.' + found_file_base
                    #found_file = parse_directory_path('module_path', found_file) + '.' + found_file_base
                    found_file = parse_directory_path('module_path', found_file)[1:] + '.' + found_file_base
                    #found_file = parse_directory_path('module_path', found_file)
                return found_file
    return '< File not found >'


def initalize(
        project_path = parse_directory_path('project_path'),
        directory_omit = ['.git', '__', 'html'],
        file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']):
    """Set initial state of project start conditions.
    Establish the project directory, and return the registry."""
    # Establish working path.
    #project_path = parse_directory_path(False)
    # Identify path to 'RegistryManager.py'.
    #print(getcwd())

    # Find the file then distill it down to the relative path from projec path.
    # with that then call it with the import module.  Perhaps it would be
    # more direct if that was part of the search function.

    registry_manager_path = find_file(project_path, 'RegistryManager.py', True)
    #print(f">>registry_manager_path\n  {registry_manager_path}\n")
    print(f">>>> registry_manager_path:\n     {registry_manager_path}\n")
    print(f">>>> project_root:\n     {project_path}\n")
    print(f">>>> project_name:\n     {project_name}\n")
    print(f">>>> directory_omit:\n     {directory_omit}\n")
    print(f">>>> file_register_types:\n     {file_register_types}\n")






    # Create a registery.
    registry = importlib.import_module(
        '.Utilities.Data.Manager').Registry(
            '/home/technicus/Projects/CAD/ProjectDesignBuilder',
            ProjectDesignBuilder,
            directory_omit,
            file_register_types)




    ## Create a registery.
    #registry = import_module(
        #registry_manager_path).Registry(
            #project_root('project_path'),
            #project_name,
            #directory_omit,
            #file_register_types)   #home.technicus.Projects.CAD

    #registry = import_module(registry_manager_path).Registry(project_root(),
        #project_name, directory_omit, file_register_types)
    #registry = import_module(registry_manager_path).Registry(project_root(),
        #project_name, directory_omit, file_register_types)

    # Hand off the registry.
    #return registry

#project_path = parse_directory_path(False)
#registry_manager_path = find_file(project_path, 'RegistryManager.py')

#print(f"\ngetcwd()\n  {getcwd()}\n")
set_project_directory()
#print(f"parse_directory_path('file_path')\n  {parse_directory_path('file_path')}\n")
#print(f"parse_directory_path('project_path')\n  {parse_directory_path('project_path')}\n")
#print(f"parse_directory_path('relative_path')\n  {parse_directory_path('relative_path')}\n")

registry = initalize()

#print(f"project_path = {project_path}")
#print(f"project_root = {project_root()}")
#print(f"registry_manager_path = {registry_manager_path}\n")

#initalize(project_path = parse_directory_path(False))
