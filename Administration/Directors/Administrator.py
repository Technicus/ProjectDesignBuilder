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


def courier(module = None, function= None, arguments = None, directives = None,
            registry = None):
    """courier() will seek methods and classes in the project to dynamically
    facilitate transactions between functions.  It will search for modules,
    exchange arguments and returns then report to the assistant."""
    #from ast import literal_eval
    #params = "{'a': 2, 'b': 3}"
    #func(**literal_eval(params))
    #argument_eval = dict(argument.split('=') for argument in list(arguments.split(', ')))
    # >>> args = dict(e.split('=') for e in x.split(', '))
    # f (**args)
    filepath = sorted(libPath('.').glob('**/' + module + '.py'))
    module = str(filepath).split('\'')[1]
    module_name = f".{module.rsplit('/', 1)[1].strip('.py').replace('/', '.')}"
    module_path = module.rsplit('/', 1)[0].replace('/', '.')
    module = invoke(module_name, module_path)
    "headder = 'section', title = 'Report: Functions :: TEST', subtitle = None, trace_frame = True"
    #return getattr(module, function)(**argument_eval)
    if arguments == None:
        return getattr(module, function)()
    else:
        return getattr(module, function)(**literal_eval(arguments))


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
    section_report_tests_checks = courier('Typographer', 'section', "{'title' : 'Tests & Checks', 'trace_frame' : 'True'}")
    print(f"{section_report_tests_checks}")
    print(f"  Color")
    courier('Compositor', 'color_chart_256')
    invoke('.Compositor', 'Utilities.Maintenance').color_chart_256()
    print()

    # Section -> Report:Functions
    #print(f"\n{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Functions', trace_frame = True)}")
    section_report_functions = courier('Typographer', 'section', "{'title' : 'Report: Functions', 'trace_frame' : 'True'}")
    print(f"{section_report_functions}")
    print()
    for module, function_list in registry.report('functions').items():
        prefix = ''
        preferredWidth =  80
        print(f"{module}")
        for function_call, arguments in function_list.items():
            print(f"  {function_call}")
            for argument in list(arguments):
                print(f"    {argument}")
        print()

    # Section -> Footer:  Salutation
    line_test = courier(module = 'Typographer',function = 'section', arguments = "{'subtitle' : 'TEST'}")
    print(f"{line_test}")
    print(f"Test here!!!")
    print(f"{line_test}")
    # Section -> Footer: Closing
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('footer', footer_title, 'End')}\n")
