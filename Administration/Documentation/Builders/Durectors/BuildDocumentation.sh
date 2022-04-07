#!/bin/bash


#def cleanPythonOperations(operationPath, remove = False):
    #if(remove == True):
        #system(('cleanpy --all -v {}').format(operationPath))
    #else:
        #system(('cleanpy --list -v {}').format(operationPath))
        #output = sp.getoutput('whoami --version')
        #print (output)
#cleanPythonOperations(operationPath, bool(remove))



cleanpy --all -v ../ProjectDesignBuilder

# sphinx-build -b html '../ProjectDesignBuilder' '../Release/Documentation'
clear; make clean; make html