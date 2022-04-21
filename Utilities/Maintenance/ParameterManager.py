# ParameterManager.py
# 2022.04.20.21.57


#from getopt import getopt, GetoptError
#from os environ
from os import system, name, getcwd, path, mkdir, listdir, walk
#from tempfile import mkdtemp
from datetime import date, datetime
from sys import argv, exit
from sys import path as sysPath
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import configparser
#from os import system


def setParameters(returnFile = False, report = False):
    parameterFile = findFile(fileName = 'Parameters.ini')
    parameters = configparser.ConfigParser(allow_no_value=True)
    parameters.read(parameterFile)
    indent = ' '
    if(report == True):
        print('{}⦾[ {} ]'.format(indent, parameterFile))
        for section in parameters.sections():
            print('\n{}  •[ {} ]'.format(indent, section))
            for parameter in parameters[section]:
                print('{}    ○[ {} ]=( {} )'.format(indent, parameter, parameters[section][parameter]))
        print('')
    if(returnFile == False):
        return parameters
    else:
        return parameterFile
