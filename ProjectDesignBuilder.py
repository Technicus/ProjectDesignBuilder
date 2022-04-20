#!/bin/python
# ProjectDesignBuilder.py


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


def main(argv = None):
    """This is the first entry point to ProjectDesignBuilder.  The main() will act
    as the conductor of program flow between classes and other functions.

    :param argv: Takes arguments passed from terminal request,
        defaults to None

    :type argv: list, optional
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]"""

    registry = import_module(Utilities.Data.Manager.InitializationManager).initalize()
    #.Registry(project_root(), project_name, directory_omit, file_register_types)

    registry = initalize()

    return None


# The main check with one argument list.
if __name__ == "__main__":
    main(argv)
