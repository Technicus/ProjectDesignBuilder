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