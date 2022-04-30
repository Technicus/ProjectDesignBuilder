#!/bin/python


# from __future__ import absolute_import
# from ast import literal_eval
# from linecache import getline
from os import getcwd
from sys import argv
from pathlib import Path as libPath
from importlib import import_module as invoke
from datetime import datetime
# The following imports should be purged and all process that require them
# should be migrated to either typographer or compositor.  They are currently
# here only for development purposes.
from pprint import pprint, pformat
from textwrap import TextWrapper
from colorama import Fore, Back, Style
from termcolor import colored, cprint
from ast import literal_eval


project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__


def time_code():
    """Return of current date and time."""
    update_time = datetime.now()
    # timeCode = updateTime.strftime("%Y%m%d%H%M%S")
    time_code = update_time.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return time_code


def initalize(
        function = None,
        module = None,
        arguments = None,
        directives = None,
        registry = None):
    """initalize() is implemented here to find the RegistryManager module, and
    instintantiate an instance of the Registry.  This function does not
    explicitly do that, because it takes arguments for which it could be
    employed to find and instintantiate a different class object.  However,
    so far it has only one use case in returning a Regustry object."""
    filepath = sorted(libPath('.').glob('**/' + module + '.py'))
    module = str(filepath).split('\'')[1]
    module_name = f".{module.rsplit('/', 1)[1].strip('.py').replace('/', '.')}"
    module_path = module.rsplit('/', 1)[0].replace('/', '.')
    module = invoke(module_name, module_path)
    if arguments == None:
        return getattr(module, function)()
    else:
        return getattr(module, function)(**literal_eval(str(arguments)))


def registration():
    """The project administrator will process initial classes orientation then
    provide conditions for directors and managers.  This function will provoke
    the managers and directors to issue assignments.  As the conductor of
    project operations, the administrator will guide the flow of intent."""
    arguments = {}
    arguments['project_root'] = getcwd()
    arguments['project_name'] = project_name
    arguments['__version__'] = __version__
    arguments['__release__'] = __release__
    arguments['directory_omit'] = ['.git', '__', 'html']
    arguments['file_register_types'] = [
        '.md', '.py', '.rst', '.html', '.log', '.ini', '.cache']
    arguments['time_stamp'] = time_code()
    registry = initalize(
        'Registry',
        'RegistryManager',
        arguments,)
    # Now modules in the project can be imported and the registry can be
    # querried to find needed references.
    return registry


def orientation(register = None, arguments = argv):
    """In orientation() arguments, parameters, and configuration
    settings will be parsed, reviewed, interpeted and applied."""

    # Start with parsing the supplied arguments.
    from ProjectCoordinator import evaluate_arguments
    # Find the cache file, this is for creating a persistant buffer to be
    # put in place for overwriting an input prompt.
    cache_file = register.search('assistant.cache')
    # Review the cache file for development.
    print(f"\nOrientation starts here.")
    print(f"  Arguments:\n    {arguments}")
    print(f"  Cache:\n    {cache_file}\n")

    # Check the arguments.
    arguments = evaluate_arguments()
    print()

    return register

    #assistant_cache_file = open(cache_file, 'a')
    #assistant_cache_file.write('')
    #assistant_cache_file.close()

    ##print()
    ##print(evaluate_arguments(argv))
    ##print(evaluate_arguments())
    #operation = evaluate_arguments(argv).constant_value
    #if 'push' in operation:
        ##print(operation)
        #run_git(cache_file)

    #if 'publish' in operation:
        ##print(operation)
        #run_publisher()
