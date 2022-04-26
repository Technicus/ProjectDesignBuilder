#!/bin/python
# Administrator.py
# 2022.04.20.21.57


# from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from datetime import datetime
from pprint import pprint, pformat
from textwrap import TextWrapper

# from inspect import currentframe, getframeinfo, trace
# from ast import literal_eval
# from linecache import getline
from importlib import import_module as invoke
from inspect import currentframe  # , getframeinfo, trace


def time_code():
    """Return of current date and time."""
    update_time = datetime.now()
    # timeCode = updateTime.strftime("%Y%m%d%H%M%S")
    time_code = update_time.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return time_code


def assitant():
    """The project assitant will process initial classes orientation then provide
    conditions to directors and managers.  This function will provoke the
    managers and directors to issue assignments.  As the conductor of project
    flow between operations, the assistant will guide the flow of intent."""
    invoke(".Typographer", "Utilities.Maintenance").clear()
    invoke(".UtilityManager", "Utilities.Maintenance").set_project_directory()

    # Headder -> Introduction.
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('headder')}")

    # Section -> Report: arguments.
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Arguments')}")
    print(f"\nargv:\n  {argv}\n")

    # Section -> Report: Current Working Directory
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Current Working Directory')}\n")
    print(f"getcwd():\n  {getcwd()}\n")

    # Section -> Report: Initalize Registry
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Initalize Registry')}\n")
    # call initialization manager
    #print(f"initalize() registry")
    registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()

    # Section -> Report:Functions
    print(f"\n{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Functions')}")
    print()
    #print(f"*****TYPE : registry.report('functions') = {type(registry.report('functions'))}")
    #pprint(registry.report('functions'))
    for module, function_list in registry.report('functions').items():
        prefix = ''
        preferredWidth = 80
        print(f"{module}")
        for function_call in function_list:
            postfix = ' ' * (len(str(function_call).split('[')[0]) + len(str(prefix))) + '  '
            wrapper = TextWrapper(initial_indent=prefix, width=preferredWidth,
                subsequent_indent=postfix)
            #pprint(function_call, width = 79)
            #print(f"  {function_call}")
            message = function_call
            print(wrapper.fill(message))
        print()

    # Section -> Report: Classes
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Classes')}")
    print()
    for classes, class_list in registry.report('classes').items():
        prefix = ''
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
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: project_files')}")
    print()
    print(f"project_files:")
    for files in registry.report('files'):
        print(f"  {files}")
    print()

    # Section -> Report: Project Directories
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: directories')}")
    print()
    print(f"project_files:")
    for directories in registry.report('directories'):
        print(f"  {directories}")
    print()

    # Section -> Report: sysPath
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: sysPath')}")
    print()
    print(f"sysPath:")
    for paths in registry.report('sysPath'):
        print(f"  {paths}")
    print()

    # Section -> Test: Colors
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Tests & Checks')}\n")
    print(f"Color\n")
    #invoke('.Compositor', 'Utilities.Maintenance').print_format_table()
    invoke('.Compositor', 'Utilities.Maintenance').tcolor()

    # Section -> Footer:  Salutation
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'End')}")

    # Section -> Test:
    #print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section')}\n")
    #print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section')}\n")

    # Section -> Footer: Closing
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('footer')}\n")
