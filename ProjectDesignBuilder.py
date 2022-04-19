#!/bin/python
# ProjectDesignBuilder.py


from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from inspect import currentframe, getframeinfo, trace
from ast import literal_eval
from linecache import getline
import importlib
#from importlib.machinery import SourceFileLoader

__version__ = '0.0.2'
__release__ = '0.0.0'


def set_current_working_directory():
    """A utility function to find the path of current file, and change the
    current working directory from that of the execution path to the current
    file path.  It takes no arguments and returns no arguments and does not
    raise any errors."""

    if path.abspath(getcwd()) is not path.dirname(path.abspath(__file__.replace('./', ''))):
        chdir(path.dirname(path.abspath(__file__.replace('./', ''))))

    return getcwd()


def find_file(search_path = None, filename = None):
    """Search through a given path for a specified file.
    :param filename:
    :type string:
    :param search_path:
    :type string:
    :return found_file:
    :rtype string:"""

    for root, dirs, files in walk(search_path):
        found_file = ''
        for name in files:
            if name == filename:
                found_file = path.join(root, name)
                return found_file
    return '< File not found >'


def section_terminal(marker = None):
    """This funciton returns a section for printing to console or adding
    to logs to seperate process for improving readability.  It also
    provides some process information.  This can be improved with more
    development of process_inspection()."""

    if marker is None:
        marker = '='
    terminal_size = get_terminal_size()
    #terminal_size.lines
    #terminal_size.columns

    #working_file = __file__.replace('./', '')
    working_file = __file__.split('/')
    line_number = str(currentframe().f_back.f_lineno)
    section = '\n[ ' + working_file[-1] + ' ] : ' + '( ' + line_number + ' )' + \
        marker * (terminal_size.columns - len(line_number) - \
        len(working_file[-1]) - 11 )

    return section


def process_inspection(argumentation = None):
    """Returns process information that can be implemanted into
    section_terminal() to help with diagnostics.  This function needs
    some refinement to return specific information."""

    line_number = str(currentframe().f_back.f_lineno)
    arguments_caller = str(currentframe().f_back.f_locals)
    arguments_local = str(currentframe().f_locals)
    inspection = str(currentframe().f_back.f_code)
    inspection = inspection.split(',')
    inspection[0] = inspection[0].split(' ')[2]
    inspection[1] = inspection[1].split('/')[-1].replace('\"', '')
    inspection[2] = inspection[2].split(' ')[-1].replace('>', '')
    inspection.append(inspection[0])
    inspection[0] = inspection[1]
    inspection[1] = inspection[3]
    inspection[3] = line_number
    evaluation = {}
    evaluation['file'] =  inspection[0]
    evaluation['call'] =  inspection[1]
    evaluation['function'] =  inspection[2]
    evaluation['process line'] =  inspection[3]
    evaluation['call arguments'] =  literal_eval(arguments_caller)
    evaluation['current arguments'] =  literal_eval(arguments_local)
    call_file = evaluation['call arguments']['argv'][0]
    call_line = str(getline('./' + call_file, int(evaluation['process line']))).strip()
    evaluation['call line'] = call_line

    return evaluation


def process_evaluation(argument = False, evaluation = True):
    """Some kind of arbitrary test function to evaluate return variables for
    the process_inspection()."""
    return process_inspection()


def main(argv = None):
    """This is the first entry point to ProjectDesignBuilder.  The main() will act
    as the conductor of program flow between classes and other functions.

    :param argv: Takes arguments passed from terminal request,
        defaults to None

    :type argv: list, optional
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]"""

    # Report to console: file name and current function with arguments.
    print(f"{section_terminal()}")
    print(f"__file__.split('/')[-1] : __name__.split('__')[1](argv[1:])")
    print(f"{__file__.split('/')[-1]} : {__name__.split('__')[1]}({argv[1:]})")

    # Report to console: current working directory.
    print(f"{section_terminal('-')}")
    print(f"getcwd()")
    print(f"{getcwd()}")

    # Change the current working directory to file directory.
    print(f"{section_terminal('-')}")
    print(f"set_current_working_directory()")
    print(f"{set_current_working_directory()}")

    # Report to console: current working directory.
    print(f"{section_terminal('-')}")
    print(f"getcwd()")
    print(f"{getcwd()}")

    # Report to console: path to 'RegistryManager.py'.
    print(f"{section_terminal('-')}")
    print(f"1find_file({getcwd()}, 'RegistryManager.py')")
    #print(f"2{find_file(getcwd(), 'RegistryManager.py')}")
    #print(f"3{find_file(getcwd(), 'RegistryManager.py').rsplit('/',1)[0]}")
    #resistry_manager_path = str(find_file(getcwd(), 'RegistryManager.py').rsplit('/',1)[0]) + '/RegistryManager'
    #print(str(resistry_manager_path).replace('/', '.'))
    #from str(resistry_manager_path).replace('/', '.') import Registry
    #/home/technicus/Projects/CAD/ProjectDesignBuilder/Utilities/Data/Program
    #registry = import_module(find_file(getcwd(), 'RegistryManager.py'))
    #registry = importlib.import_module('/home/technicus/Projects/CAD/ProjectDesignBuilder/Utilities/Data/Program/RegistryManager')
    #from str(resistry_manager_path) import Registry
    #imporlib.find_module(RegistryManager, .home.technicus.Projects.CAD.ProjectDesignBuilder.Utilities.Data.Program)
    #importlib._abc.Finder(RegistryManager, 'ProjectDesignBuilder/Utilities/Data/Program')
    #from Utilities.Data.Program.RegistryManager import Registry
    #reger = importlib.import_module(Utilities.Data.Program.RegistryManager.Registry)

    #https://tutorial.eyehunts.com/python/python-import-module-from-path-example-code/
    #registry = SourceFileLoader("Registry", "Utilities/Data/Program/RegistryManager.py").load_module('/home/technicus/Projects/CAD', 'ProjectDesignBuilder')

    #spec = importlib.util.spec_from_file_location("Registry", "Utilities/Data/Program/RegistryManager.py")

    #registry = importlib.util.module_from_spec(spec)

    #spec.loader.exec_module(registry)

    #print(registry)

    # imports the module from the given path
    #foo = SourceFileLoader("piss", "Utilities/Data/Program/main.py").load_module()

    #print(foo)

    #import importlib.util

    #spec = importlib.util.spec_from_file_location("piss", "Utilities/Data/Program/Pisser.py")

    #foo = importlib.util.module_from_spec(spec)

    #spec.loader.exec_module(foo)

    piss = importlib.import_module('Utilities.Data.Program.Pisser')

    #foo.pissAss()
    print(piss)



    ''' This is a test section for helping with development of
    process_inspection().'''
    print(f"{section_terminal('-')}")
    for report, analysis in process_inspection().items():
        if type(analysis) is dict:
            for arguments, variables in analysis.items():
                print(f"{type(variables)} :: {arguments} :: {variables} ")
        else:
            print(f"{type((analysis))} :: {report} :: {analysis} ")
    print(f"{section_terminal()}\n")

# The main check with one argument list.
if __name__ == "__main__":
    main(argv)
