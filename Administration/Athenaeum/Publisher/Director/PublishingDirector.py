#!/bin/python

from os import path, getcwd, chdir
from PublishingManagement import Registry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, CRITICAL, getLogger
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


def log_register(registry = None, logger = None):
    logger.info(registry)
    logger.info(registry.search())
    logger.info(registry.report())
    logger.info(sysPath)
    logger.info(logger)


#def setup_logger():
    ## Setup an configure logging from config file.
    #log_file_config = registry.search(query = 'Logger_Documentum.ini',
        #dir_file = 'file')
    #logging.config.fileConfig(log_file_config)
    #logger = getLogger('Director')
    #return logger

def build_documentation(registry = None):
    from Author import document_builder
    document_builder(registry)

def main():
    indent = ['', '  ', '    ', '        ']
    project_name = 'ProjectDesignBuilder'

    # Generate a project registry
    set_current_working_directory()

    # Establish argument variables to create registry
    project_path = getcwd().split(project_name)
    project_root = project_path[0] + project_name
    directory_omit = ['.git', '__']
    file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']

    # Create the registry
    registry = Registry(project_root, project_name, directory_omit,
        file_register_types)

    # Update sysPath with registry directory information.
    set_sysPath(registry)

    # Setup an configure logging from config file.
    log_file_config = registry.search(query = 'Logger_Documentum.ini', dir_file = 'file')
    logging.config.fileConfig(log_file_config)
    log_director = getLogger('Director')

    log_register(registry, log_director)

    build_documentation(registry)









    # Create some arbitrary log messages to test functionality.
    # Some messages go to console, some go to file.
    #log_director.debug('This message should appear in the log file')
    #log_director.info('So should this')
    #log_director.warning('And this, too')
    #log_director.debug('This message should go to the log file')
    #log_director.info('So should this')
    #log_director.warning('And this, too')
    #log_director.error('And non-ASCII stuff, too, like Øresund and Malmö')
    #log_director.critical('This message should appear on the console.')


if __name__ == "__main__":
    main()
