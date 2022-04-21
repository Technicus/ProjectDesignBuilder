#!/bin/python
# InitializationManager.py
# 2022.04.20.21.57


#from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
#from inspect import currentframe, getframeinfo, trace
#from ast import literal_eval
#from linecache import getline
from importlib import import_module as invoke
from inspect import currentframe #, getframeinfo, trace


project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__


def section(headder = 'section'):
    working_file = str(__file__.split('/')[-1])
    title = f"[ {working_file} : {str(currentframe().f_back.f_lineno)} ]"
    project_time = invoke('.UtilityManager', 'Utilities.Maintenance').time_code()
    if headder == 'headder':
        title = f"[ {project_name}, {__release__}/{__version__} ] :: ( {project_time} )"
        return invoke('.Typographer', 'Utilities.Maintenance').headding_section(marker = None, title = title)
    if headder == 'footer':
        return invoke('.Typographer', 'Utilities.Maintenance').headding_section(marker = None, title = title)
    if headder == 'section':
        return invoke('.Typographer', 'Utilities.Maintenance').headding_section(marker = '-', title = title)


def assitant():
    """The project assitant will process initial class orientation then provide
    conditions to directors and managers.  This function will provoke the
    managers and directors to issue assignments.  As the conductor of project
    flow between operations, the assistant will guide the flow of intent."""
    invoke('.Typographer', 'Utilities.Maintenance').clear()
    invoke('.UtilityManager', 'Utilities.Maintenance').set_project_directory()
    #invoke('','Utilities.Maintenance').()
    #print(f"{headding_initial}")
    print(f"{section('headder')}")
    print(f"\nargv :: {argv}")
    print(f"{section('section')}\n")
    print(f"getcwd() :: {getcwd()}")
    print(f"{section('footer')}\n")


