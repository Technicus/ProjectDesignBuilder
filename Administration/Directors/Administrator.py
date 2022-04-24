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
    # invoke('','Utilities.Maintenance').()
    # print(f"{headding_initial}")
    print(f"{invoke('.Compositor', 'Utilities.Maintenance').section('headder')}")
    print(f"\nargv :: {argv}")
    #print(f"{invoke(".UtilityManager.Typographer", "Utilities.Maintenance").section('section')}\n")
    #print(f"getcwd() :: {getcwd()}")
    #print(f"{invoke(".UtilityManager.Typographer", "Utilities.Maintenance").section('footer')}\n")
