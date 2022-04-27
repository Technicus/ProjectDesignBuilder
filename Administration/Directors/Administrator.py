#!/bin/python
# Administrator.py
# 2022.04.20.21.57


# from __future__ import absolute_import
# from ast import literal_eval
# from linecache import getline
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from pathlib import Path as libPath
from importlib import import_module as invoke, util
from inspect import currentframe  # , getframeinfo, trace
from datetime import datetime
# The following imports should be purged and all process that require them
# should be migrated to either typographer or compositor.  They are currently
# here only for development purposes.
from pprint import pprint, pformat
from textwrap import TextWrapper
from colorama import Fore, Back, Style
from termcolor import colored, cprint


project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__


def time_code():
    """Return of current date and time."""
    update_time = datetime.now()
    # timeCode = updateTime.strftime("%Y%m%d%H%M%S")
    time_code = update_time.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return time_code


def courier(module = None, function= None, arguments = None, directives = None,
            registry = None):
    """courier() will seek methods and classes in the project to dynamically
    facilitate transactions between functions.  It will search for modules,
    exchange arguments and returns then report to the assistant."""
    filepath = sorted(libPath('.').glob('**/' + module + '.py'))
    module = str(filepath).split('\'')[1]
    module_name = f".{module.rsplit('/', 1)[1].strip('.py').replace('/', '.')}"
    module_path = module.rsplit('/', 1)[0].replace('/', '.')
    module = invoke(module_name, module_path)
    return getattr(module, function)(arguments)


def assitant():
    """The project assitant will process initial classes orientation then provide
    conditions to directors and managers.  This function will provoke the
    managers and directors to issue assignments.  As the conductor of project
    flow between operations, the assistant will guide the flow of intent."""
    invoke(".Typographer", "Utilities.Maintenance").clear()
    invoke(".UtilityManager", "Utilities.Maintenance").set_project_directory()

    headder_title = f"{project_name}, {__release__}/{__version__} :: {time_code()}"
    footer_title = f"{project_name}, {__release__}/{__version__} :: {time_code()}"

    # Headder -> Introduction.
    cprint(f"{invoke('.Typographer', 'Utilities.Maintenance').section('headder', headder_title, 'Start')}", 'green')

    # Section -> Report: arguments.
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', title = 'Report: Arguments', trace_frame = True)}")
    print(f"\nargv:\n  {argv}\n")

    # Section -> Report: Current Working Directory
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Current Working Directory', trace_frame = True)}\n")
    print(f"getcwd():\n  {getcwd()}\n")

    # Section -> Report: Initalize Registry
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Initalize Registry', trace_frame = True)}\n")
    # call initialization manager
    #print(f"initalize() registry")
    registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()

    # Section -> Report: Classes
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Classes', trace_frame = True)}")
    print()
    for classes, class_list in registry.report('classes').items():
        prefix = '  '
        preferredWidth = 80
        print(f"{classes}")
        for classes in class_list:
            postfix = ' ' * (len(str(classes).split('[')[0]) + len(str(prefix))) + '  '
            wrapper = TextWrapper(initial_indent=prefix, width=preferredWidth,
                subsequent_indent=postfix)
            message = classes
            print(wrapper.fill(message))
    print()

    # Section -> Report: Project Files
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: project_files', trace_frame = True)}")
    print()
    print(f"project_files:")
    for files in registry.report('files'):
        print(f"  {files}")
    print()

    # Section -> Report: Project Directories
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: directories', trace_frame = True)}")
    print()
    print(f"project_directories:")
    for directories in registry.report('directories'):
        print(f"  {directories}")
    print()

    # Section -> Report: sysPath
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: sysPath', trace_frame = True)}")
    print()
    print(f"sysPath:")
    for paths in registry.report('sysPath'):
        print(f"  {paths}")
    print()

    # Section -> Test: Colors
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Tests & Checks', trace_frame = True)}\n")
    print(f"  Color")
    #invoke('.Compositor', 'Utilities.Maintenance').print_format_table()
    invoke('.Compositor', 'Utilities.Maintenance').color_chart_256()
    print()

    # Section -> Report:Functions
    print(f"\n{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Functions', trace_frame = True)}")
    print()
    #print(f"*****TYPE : registry.report('functions') = {type(registry.report('functions'))}")
    #pprint(registry.report('functions'))
    for module, function_list in registry.report('functions').items():
        prefix = ''
        preferredWidth =  80
        print(f"{module}")
        for function_call, arguments in function_list.items():
            print(f"  {function_call}")
            #print(f"    {str(arguments)}")
            for argument in list(arguments):
                print(f"    {argument}")
                #if len(argument[0]) > 0:
                    ##for argument in argument_list:
                    #print(f"    {argument}")
        print()

    # Section -> Footer:  Salutation
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section')}")

    # Section -> Test:
    #print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section')}\n")
    #print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section')}\n")
    test = 'test'
    #section = courier(module = 'Typographer.py', function = 'section', arguments = 'section')('section')
    #courier(module = 'Typographer.py')
    #print(f"{courier(module = 'Typographer.py', function = 'section', arguments = 'section')('section')}")
    section = courier(module = 'Typographer', function = 'section', arguments = 'section')
    print(f"{section}")
    print(f"{test}")
    print(f"{courier(module = 'Typographer', function = 'section', arguments = 'section')}")
    #print(f"{section}")('section')
    print(f"{section}")

    # Section -> Footer: Closing
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('footer', footer_title, 'End')}\n")
