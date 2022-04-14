#!/bin/python

from os import path, getcwd, chdir
from PublishingManagement import Registry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, getLogger
import logging.config
from sys import path as sysPath


def set_current_working_directory():
    if path.abspath(getcwd()) is not path.dirname(path.abspath(__file__)):
        chdir(path.dirname(path.abspath(__file__)))

def set_sysPath(registry):
    #for register, field in registry.report().items():
        #for entery in field:
    #print(registry.report('path'))
    for directory in registry.report('path').get('project_directories'):
        #print(directory)
        project_path = str(
            ''.join(registry.report('path').get('project_root'))) + '/' \
            + str(directory).lstrip('./')
        sysPath.append(project_path)


def main():
    indent = ['', '  ', '    ', '        ']
    project_name = 'ProjectDesignBuilder'

    # Generate a project registry
    set_current_working_directory()

    # Establish argument variables to create registry
    project_path = getcwd().split(project_name)
    project_root = project_path[0] + project_name
    directory_omit = ['.git', '__']
    file_register_types = ['.md', '.py', '.rst', '.html', '.log']

    # Create the registry
    registry = Registry(project_root, project_name, directory_omit,
        file_register_types)
    #registry.report(report_file = 'console')

    # Update sysPath with registry directory information
    set_sysPath(registry)

    #log_file_config = './Utilities/Maintenance/Logger.ini'
    log_file_config = './Utilities/Maintenance/Logger.ini'
    #config.fileConfig(log_file_config, disable_existing_loggers=False)
    #config.fileConfig(log_file_config)
    logging.config.fileConfig(log_file_config)
    logger_primary = getLogger('primaryLogger')
    logger_primary.debug('This message should appear on the console')
    logger_primary.info('So should this')
    logger_primary.warning('And this, too')
    logger_primary.debug('This message should go to the log file')
    logger_primary.info('So should this')
    logger_primary.warning('And this, too')
    logger_primary.error('And non-ASCII stuff, too, like Øresund and Malmö')
    #print(log_file_config)


if __name__ == "__main__":
    main()
