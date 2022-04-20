#!/bin/python
# ProjectDesignBuilder_01.py


from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from inspect import currentframe, getframeinfo, trace
from ast import literal_eval
from linecache import getline
from importlib import import_module

project_name = 'ProjectDesignBuilder'
__version__ = '0.0.2'
__release__ = '0.0.0'


def project_root():
    """Change the current working directory to project root directory."""

    #project_root = set_current_working_directory()
    project_root = getcwd()
    project_path = project_root[0] + project_name

    return project_root


# Report to console: path to 'RegistryManager.py'.
directory_omit = ['.git', '__', 'html']
file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']

#for directories in walk(getcwd()):
for project_directory, pdirs, pfiles in walk(project_root()):
    for subdir in pdirs:
        path_discovery = str(path.join(project_directory, subdir))
        if any(omission in path_discovery for omission in
            directory_omit):
            pass
        else:
            print(path_discovery)

    review(registry)
    evaluation(registry)
