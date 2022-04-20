#!/bin/python

from os import system, name, execv
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import re

# Clear the terminal
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

# Call the watch dog
def watchCall(openFile = ''):
    subprocess.call(openFile, shell=True)
    #cmd = '. $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate my-rdkit-env'
    #cmd = 'source $HOME/miniforge/bin/activate && conda activate cadquery-dev && cq-editor ./cabinet.py'
    #cmd = 'source $HOME/miniforge/bin/activate && conda activate cadquery-dev && cq-editor ', openFile
    #subprocess.Popen(cmd, shell=True)
    #subprocess.call(cmd, shell=True, executable='/bin/bash')
    #subprocess.call(cmd, shell=True, executable='cq-editor')
    #print("Process open!")


class DirectoryMonitor:
    # Set the directory on watch
    watch = "./"
    def __init__(self):
        self.observer = Observer()
    def run(self):
        event_handler = Handler()
        event_handler.watch = self.watch
        self.observer.schedule(event_handler, self.watch, recursive = True)
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
        fileType = re.split("[_.]", event.src_path)[-1]
        eventFile = event.src_path

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            if(fileType != 'kate-swp'):
                print('\nWatchdog event = [ created ] : [ % s ]' % event.src_path)
                #clear()
                #watchCall(event.src_path)

        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            #clear()
            if(fileType != 'kate-swp'):
                if (event.src_path == sys.argv[0]):
                    print('Watchdog event = [ modified ] : [ % s ]\n' % event.src_path)
                    #print('eventFile : SELF!!!'.format(eventFile))
                    #watchCall(event.src_path)
                    #execv(sys.argv[0], sys.argv)
                else:
                    #print('eventFile : {}'.format(eventFile))
                    print('Watchdog event = [ modified ] : [ % s ]\n' % event.src_path)
                if (event.src_path == './ProjectDesignBuilder.py'):
                    watchCall(event.src_path)
                if (event.src_path == './Utility.py'):
                    watchCall('./ProjectDesignBuilder.py')
                if (event.src_path == './Parameters.ini'):
                    watchCall('./ProjectDesignBuilder.py')
                if (event.src_path == './Craft.py'):
                    watchCall('./ProjectDesignBuilder.py')
                if (event.src_path == './Cabinet.py'):
                    watchCall('./ProjectDesignBuilder.py')

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #clear()
    watch = DirectoryMonitor()
    watch.watchDirectory = path
    watch.run()











### Scraps
            #position = eventFile.index('.') # gets position of the . in the filename
            #fileType = eventFile[1:position]
            #print('\nfileType : {}'.format(fileType))
                #print(fileType)
            #else:

#if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO,
                        #format='%(asctime)s - %(message)s',
                        #datefmt='%Y-%m-%d %H:%M:%S')
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #event_handler = LoggingEventHandler()
    #event_handler = clear(LoggingEventHandler)

    #observer = Observer()
    #observer.schedule(event_handler, path, recursive=True)
    #observer.start()
    #try:
        #while True:
            #time.sleep(1)
    #except KeyboardInterrupt:
        #observer.stop()
    #observer.join()
    ##functionStatus()
