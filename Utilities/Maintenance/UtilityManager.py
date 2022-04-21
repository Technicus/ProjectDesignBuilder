# UtilityManager.py
# 2022.04.20.21.57


from importlib import import_module as invoke
from os import system, getcwd, path, chdir
from datetime import datetime


project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__


def time_code():
    """Return of current date and time."""
    update_time = datetime.now()
    # timeCode = updateTime.strftime("%Y%m%d%H%M%S")
    time_code = update_time.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return time_code


def parse_directory_path(project_root = 'file_path', parse_file = __file__):
    """Formerly known as set_project_directory(). A utility function to find
    the path of current file, and change the current working directory from
    that of the execution path to the current file path.  It takes one
    argument and returns a ptath variation.  It has no error handler."""
    if project_root == 'file_path':
        return path.dirname(path.abspath(parse_file.replace('./', '')))
    if project_root == 'project_path':
        return path.dirname(path.abspath(parse_file.replace('./', ''))).split(project_name)[0] + project_name
    if project_root == 'relative_path':
        return parse_directory_path('file_path').replace(parse_directory_path('project_path') + '/', './')
    if project_root == 'module_path':
        return parse_directory_path('file_path').replace(parse_directory_path('project_path') + '/', '.').replace('/', '.')


def set_project_directory():
    """This function was extracted from parse_directory_path.  It changes
    the current working directory to the project directory."""
    if path.abspath(getcwd()) is not parse_directory_path('project_path'):
        chdir(parse_directory_path('project_path'))
    return None


def clean_python_operations(operation_path, remove = False):
    if(remove == True):
        system(('cleanpy --all -v {}').format(operation_path))
    else:
        system(('cleanpy --list -v {}').format(operation_path))
        #output = sp.getoutput('whoami --version')
        #print (output)
