#!/bin/python

#from sys import path as sysPath, executable
#from os import system, path, getcwd, chdir, scandir, listdir, walk
#from os.path import relpath
#import subprocess
#import logging
#from termcolor import colored
from os import path, getcwd
from Registry import registry, registry_report, registry_query
from RegistryClass import ProjectRegistry


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


def main():
    indent = ['', '  ', '    ', '        ']
    project_name = 'ProjectDesignBuilder'
    print('[[ {} ]]\n'.format(path.basename(__file__)))

    # Generate a project registry
    print('{}>>> [ registry() ]:\n'.format(indent[0]))
    project_path = getcwd().split(project_name)
    project_root = project_path[0] + project_name
    file_register_types = ['.md', '.py', '.rst', '.html']
    directory_omit = ['.git', '__']
    registry_report(registry(project_root, project_name, directory_omit,
                            file_register_types))
    registry_query(registry(project_root, project_name, directory_omit,
                           file_register_types), ['Room.py', 'sandbox.py'])
    #registry = ProjectRegistry(project_root, project_name, directory_omit,
        #file_register_types)
    #registry.report()
    #for register, field in registry(project_root, project_name, directory_omit,
        #file_register_types).items():
        #print('{}{}:'.format(indent[1], register,))
        #for entery in field:
            #print('{}{}'.format(indent[2], entery))
        #print()


if __name__ == "__main__":
    main()
