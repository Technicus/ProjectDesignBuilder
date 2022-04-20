#!/bin/python
# ProjectDesignBuilder_01.py


from __future__ import absolute_import
from os import getcwd, path, chdir, mkdir, walk, get_terminal_size
from sys import argv
from inspect import currentframe, getframeinfo, trace
from ast import literal_eval
from linecache import getline
from importlib import import_module


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


def _section(marker = None):
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
    _section() to help with diagnostics.  This function needs
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
    print(f"{_section()}\n")
    print(f"__file__.split('/')[-1] : __name__.split('__')[1](argv[1:])")
    print(f"{__file__.split('/')[-1]} : {__name__.split('__')[1]}({argv[1:]})")

    # Report to console: current working directory.
    print(f"{_section('-')}")
    print(f"\ngetcwd()")
    print(f"{getcwd()}")

    # Change the current working directory to file directory.
    print(f"{_section('-')}")
    project_name = 'ProjectDesignBuilder'
    project_root = set_current_working_directory()
    project_path = project_root[0] + project_name
    print(f"\nproject_name = {project_name}")
    print(f"set_current_working_directory()")
    print(f"project_path = set_current_working_directory()")
    print(f"{project_path}")

    # Report to console: current working directory.
    print(f"{_section('-')}")
    print(f"\ngetcwd()")
    print(f"{getcwd()}")

    # Report to console: path to 'RegistryManager.py'.
    print(f"{_section('-')}\n")
    registry_manager_path = find_file(getcwd(), 'RegistryManager_01.py')
    registry_manager_path = registry_manager_path.replace(getcwd(), '')
    registry_manager_path = registry_manager_path.replace('/', '.').split('.', 1)[1]
    registry_manager_path = registry_manager_path.rsplit('.', 1)[0]
    print(f"{registry_manager_path}")

    # Establish argument variables to create registry
    print(f"{_section('-')}")
    #project_path = getcwd().split(project_name)
    #project_root = project_path[0] + project_name
    directory_omit = ['.git', '__', 'html']
    file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']
    print(f"\ndirectory_omit = {directory_omit}")
    print(f"file_register_types = {file_register_types}")
    print(f"project_path = {project_path}")
    print(f"project_root = {project_root}")

    # Create a registery.
    print(f"{_section('-')}")
    print(f"\nCreate registry.")
    #registry = import_module('Utilities.Data.Program.RegistryManager_01').Registry()
    registry = import_module(registry_manager_path).Registry(project_root,
        project_name, directory_omit, file_register_types)

    print(f"{_section('-')}")
    print(f"\nregistry = {registry}")

    print(f"{_section('-')}")
    print(f"\nproperty_and_method for registry:")
    for property_and_method in dir(registry):
        if property_and_method.find('__'):
            print(f"  {property_and_method}")

    print(f"{_section('-')}")
    #print(f"registry.report()[0].items()")
    for register, listing in registry.report()[0].items():
        print(f"\n{register}:")
        for value in listing:
            print(f"  {value}")
        print(f"{_section('-')}")

    #print(f"{_section('-')}")
    print(f"\nregistry.report()[1]")
    for register in registry.report()[1]:
        print(f"  {register}")

    print(f"{_section('-')}")
    #print(f"registry.search('Map') = {registry.search('Map', dir_file = 'directory')}")
    #print(f"registry.search('ProjectDesignBuilder.mm') = {registry.search('ProjectDesignBuilder.mm', dir_file = 'file')}")
    #print(f"{_section()}\n")

    # Test section
    ''' Search test '''
    #print(registry.report('sysPath'))
    #registry.report_cache_files()
    #print(f"\nregistry.search() = {registry.search()}")
    registry.set_sysPath()
    #Registry set_sysPath() test.
    #registry.set_sysPath(update_sysPath = True)
    ##for path in registry.report('sysPath'):
    #for path in registry.report('sysPath'):
        #print(f"  {path}")
    print(f"{_section()}\n")


# The main check with one argument list.
if __name__ == "__main__":
    main(argv)
