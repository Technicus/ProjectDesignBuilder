#!/bin/python
# Administrator.py
# 2022.04.20.21.57


# from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from datetime import datetime


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
    """The project assitant will process initial class orientation then provide
    conditions to directors and managers.  This function will provoke the
    managers and directors to issue assignments.  As the conductor of project
    flow between operations, the assistant will guide the flow of intent."""
    invoke(".Compositor", "Utilities.Maintenance").clear()
    invoke(".UtilityManager", "Utilities.Maintenance").set_project_directory()
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('headder')}")
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'Arguments')}")
    print(f"\nargv :: {argv}\n")
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'Current Working Directory')}\n")
    print(f"getcwd() :: {getcwd()}\n")
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'Initalize Registry')}\n")
    # call initialization manager
    print(f"initalize() registry")
    registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()
    print(f"\n{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'Functions')}")
    print()
    for module, function_list in registry.functions().items():
        print(f"{module}")
        for function_call in function_list:
            print(f"  {function_call}")
        print()
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'Classes')}")

    print()
    for class_, class_list in registry.classes().items():
        print(f"{class_}")
        for class__ in class_list:
            print(f"  {class__}")
        print()
    #for search in registry.search('.py'):
        #with open(search) as project_file:
            #if 'class' in project_file.read():
                #search = search.split("/")[-1]
                #print(f"{search}")
                #project_file.seek(0)
                #for line in project_file:
                    #if line.startswith("class "):
                        #line = line.replace(":\n", "")
                        #print(f"  {line}")
                #print()

    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section', 'End')}")

    #print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section')}\n")
    #print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section')}\n")
    #print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('section')}\n")
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('footer')}\n")
