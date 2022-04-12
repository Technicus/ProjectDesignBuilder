#!/bin/python

#from sys import path as sysPath, executable
#from os import system, path, getcwd, chdir, scandir, listdir, walk
#from os.path import relpath
#import subprocess
#from termcolor import colored
from os import path, getcwd, chdir
#from Registry import registry, registry_report, registry_query
from RegistryClass import ProjectRegistry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR


def run_sphinx_build():
    #conf_path = ? # Path to conf.py file
    #path_doc_tree = ? # Path to .doctree files
    #log_warrning_error = ? # Warning and error log file.
    #path_source = ?
    #path_output = ?
    # sphinx-build [options] <sourcedir> <outputdir> [filenames …]
    call_sphinx_build = (
        'sphinx-build -b html -a -E -c' + conf_path + '-d' +
        path_doc_tree + '-n -v -w' + log_warrning_error +
        '--keep-going' + path_source + path_output)
    subprocess_test = subprocess.run(
        call_Sphinx-Build, stdin=None, input=None,
        stdout=None, stderr=None, capture_output=True,
        shell=True, cwd=None, timeout=None, check=False,
        encoding=None, errors=None, text=None,
        env={'PYTHONPATH':python_path},universal_newlines=None)
    system((
        'sphinx-apidoc -f -o {} {}').format('../../Editors',
        directory_comprehension()['dir_project_design_builder_absolute']))


def run_sphinx_apidoc():
    subprocess_test = subprocess.run(
        './test.py', stdin=None, input=None, stdout=None, stderr=None,
        capture_output=True, shell=True, cwd=None, timeout=None,
        check=False, encoding=None, errors=None, text=None,
        env={'PYTHONPATH':python_path}, universal_newlines=None)


def run_TOC_tree():
    subprocess_test = subprocess.run(
        './test.py', stdin=None, input=None, stdout=None, stderr=None,
        capture_output=True, shell=True, cwd=None, timeout=None,
        check=False, encoding=None, errors=None, text=None,
        env={'PYTHONPATH':python_path}, universal_newlines=None)

def set_current_working_directory():
    print(f'`path.abspath(getcwd())`:\n[ {path.abspath(getcwd())} ]\n')
    print(f'`path.dirname(path.abspath(__file__))`:\n[ {path.dirname(path.abspath(__file__))} ]\n')
    if path.abspath(getcwd()) is not path.dirname(path.abspath(__file__)):
        chdir(path.dirname(path.abspath(__file__)))
    print(f'`path.abspath(getcwd())`:\n[ {path.abspath(getcwd())} ]\n')
    print(f'`path.dirname(path.abspath(__file__))`:\n[ {path.dirname(path.abspath(__file__))} ]\n')

def main():

    #debug('This message should go to the log file')
    #info('So should this')
    #warning('And this, too')
    #error('And non-ASCII stuff, too, like Øresund and Malmö')
    set_current_working_directory()
    basicConfig(filename='../Logs/publisher.log', filemode='w',encoding='utf-8', level=DEBUG)

    indent = ['', '  ', '    ', '        ']

    project_name = 'ProjectDesignBuilder'

    info('[[ {} ]]\n'.format(path.basename(__file__)))

    print('[[ {} ]]\n'.format(path.basename(__file__)))

    # Generate a project registry
    info('{}>>> [ main() ]:\n'.format(indent[0]))

    print('{}>>> [ main() ]:\n'.format(indent[0]))

    project_path = getcwd().split(project_name)

    info('[ project_path ]\n\t[ {} ]\n'.format(project_path))

    project_root = project_path[0] + project_name

    info('[ project_root ]\n\t[ {} ]\n'.format(project_root))

    file_register_types = ['.md', '.py', '.rst', '.html']

    directory_omit = ['.git', '__']


    #registry_report(registry(project_root, project_name, directory_omit,
                            #file_register_types))

    #registry_query(registry(project_root, project_name, directory_omit,
                           #file_register_types), ['Room.py', 'sandbox.py'])

    registry = ProjectRegistry(project_root, project_name, directory_omit,
        file_register_types)
    registry.report()
    #for register, field in registry(project_root, project_name, directory_omit,
        #file_register_types).items():
        #print('{}{}:'.format(indent[1], register,))
        #for entery in field:
            #print('{}{}'.format(indent[2], entery))
        #print()


if __name__ == "__main__":
    main()
