#!/bin/python

from os import system
from sys import argv
#import subprocess as sp

operationPath = argv[1] if len(argv) > 1 else './'
remove = argv[2] if len(argv) > 2 else False
#print(operationPath)
#print(remove)

def cleanPythonOperations(operationPath, remove = False):
    if(remove == True):
        system(('cleanpy --all -v {}').format(operationPath))
    else:
        system(('cleanpy --list -v {}').format(operationPath))
        #output = sp.getoutput('whoami --version')
        #print (output)
cleanPythonOperations(operationPath, bool(remove))
