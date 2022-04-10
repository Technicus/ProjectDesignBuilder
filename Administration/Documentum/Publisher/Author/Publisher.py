#!/bin/python

#from sys import path as sysPath, executable
#from os import system, path, getcwd, chdir, scandir, listdir, walk
#from os.path import relpath
#import subprocess
#import logging
#from termcolor import colored
from os import path, getcwd
from Registry import registry


def runSphinx_biuld():
    #confPath = ? # Path to conf.py file
    #pathDocTree = ? # Path to .doctree files
    #logWarrningError = ? # Warning and error log file.
    #pathSource = ?
    #pathOutput = ?
    # sphinx-build [options] <sourcedir> <outputdir> [filenames …]
    callSphinx_Build = 'sphinx-build -b html -a -E -c' + confPath + '-d' + pathDocTree + '-n -v -w' + logWarrningError + '--keep-going' + pathSource + pathOutput
    subProcessTest = subprocess.run(callSphinx-Build, stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)
    system(('sphinx-apidoc -f -o {} {}').format('../../Editors', directoryComprehension()['dirProjectDesignBuilder_Absolute']))
def runSphinx_apidoc():
    subProcessTest = subprocess.run('./test.py', stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)

def runTOC_tree():
    subProcessTest = subprocess.run('./test.py', stdin=None, input=None, stdout=None, stderr=None,
                                  capture_output=True, shell=True, cwd=None, timeout=None,
                                  check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                                  universal_newlines=None)


def main():
    indent = ['', '  ', '    ', '        ']
    projectName = 'ProjectDesignBuilder'
    print('[[ {} ]]\n'.format(path.basename(__file__)))
    # Generate a project registry
    print('{}>>> [ registry() ]:\n'.format(indent[0]))

    projectPath = getcwd().split(projectName)
    projectRoot = projectPath[0] + projectName
    fileRegisterTypes = ('.md', '.py', '.rst', '.html')
    directoryOmit = ('.git', '__')
    for register, field in registry(projectRoot, projectName, directoryOmit, fileRegisterTypes).items():
        print('{}{}:'.format(indent[1], register,))
        for entery in field:
            print('{}{}'.format(indent[2], entery))
        print()


    #print('\n{}>>> Call to test.py:\n'.format(indent[0]))
    #print('{}sysPath test.py:'.format(indent[1]))
    #for address in sysPath:
      #print('{}{}'.format(indent[2], address))
    #print('{}'.format(indent[0]))
    #print(colored('hello', 'red'), colored('world', 'green'))
    #variableTest = ['test_00', 'test_01']
    #return  = variableTest


if __name__ == "__main__":
    main()
