#!/bin/python

from sys import path as sysPath
from os import walk, path, getcwd, system, scandir, listdir
from os.path import relpath

#from termcolor import colored


indent = ['', '  ', '    ', '        ']

print('\n{}>>> Call to test.py:\n'.format(indent[0]))
#print('{}sysPath test.py:'.format(indent[1]))
#for address in sysPath:
  #print('{}{}'.format(indent[2], address))
#print('{}'.format(indent[0]))

#print(colored('hello', 'red'), colored('world', 'green'))

variableTest = ['test_00', 'test_01']

return  = variableTest


def runSphinx-biuld():
    confPath = ? # Path to conf.py file
    pathDocTree = ? # Path to .doctree files
    logWarrningError = ? # Warning and error log file.
    pathSource = ?
    pathOutput = ?
    # sphinx-build [options] <sourcedir> <outputdir> [filenames …]
    callSphinx-Build = 'sphinx-build -b html -a -E -c' + confPath + '-d' + pathDocTree + '-n -v -w' + logWarrningError + '--keep-going' + pathSource + pathOutput
    subProcessTest = subprocess.run(callSphinx-Build, stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)

system(('sphinx-apidoc -f -o {} {}').format('../../Editors', directoryComprehension()['dirProjectDesignBuilder_Absolute']))
def runSphinx-apidoc():
    subProcessTest = subprocess.run('./test.py', stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)

def runTOC-tree():
    subProcessTest = subprocess.run('./test.py', stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)
