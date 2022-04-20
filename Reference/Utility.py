#!/bin/python

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


#def cleanPythonOperations(operationPath, remove = False):
    #if(remove == True):
        #system(('cleanpy --all -v {}').format(operationPath))
    #else:
        #system(('cleanpy --list -v {}').format(operationPath))
        #output = sp.getoutput('whoami --version')
        #print (output)
#cleanPythonOperations(operationPath, bool(remove))

# Clear the terminal
def clear():
    """This function clears the screen."""
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

# Return a formatted time string "year-month-day-hour-minute-second"
def updateTimeCode():
    functionStatus()
    updateTime = datetime.now()
    # timeCode = updateTime.strftime("%Y%m%d%H%M%S")
    timeCode = updateTime.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return timeCode

def findFile(fileName = ''):
    for workPath in sysPath:
        for root, dirs, files in walk(workPath):
            for name in files:
                # As we need to get the provided python file,
                # comparing here like this
                if(name == fileName):
                    foundFile = path.abspath(path.join(root, name))
                    print('Found:\n[{}]\n'.format(foundFile))
    return foundFile

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

def setDirectories(report = False, parameterSet = ''):
    indent = ' '
    print('{}⦾[ {} ]\n'.format(indent, parameterSet))
    for parameter in parameterSet:
        print('{}    ○[ {} ]=( {} )'.format(indent, parameter, parameterSet[parameter]))




# Start cq-editor
def startCadQueryEditor(openFile = ''):
    #cmd = '. $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate my-rdkit-env'
    #cmd = 'source $HOME/miniforge/bin/activate && conda activate cadquery-dev && cq-editor ./cabinet.py'
    cmd = 'source $HOME/miniforge/bin/activate && conda activate cadquery-dev && cq-editor ', openFile
    #subprocess.call(cmd, shell=True)
    subprocess.Popen(cmd, shell=True)
    #subprocess.call(cmd, shell=True, executable='/bin/bash')
    #subprocess.call(cmd, shell=True, executable='cq-editor')
    print("Process open!")


# Create a watcher to observe file modifications
class FileWatcher:
    # Set the directory on watch
    watchTarget = "./"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchTarget, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            #LoggingEventHandler()
            subprocess.call("./Cabinet.py", shell=True)
