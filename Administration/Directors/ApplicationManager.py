
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

#ApplicationManager.py
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