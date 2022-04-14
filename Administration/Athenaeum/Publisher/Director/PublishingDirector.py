#!/bin/python

#from sys import path as sysPath, executable
#from os import system, path, getcwd, chdir, scandir, listdir, walk
#from os.path import relpath
#import subprocess
#from termcolor import colored
#from Registry import registry, registry_report, registry_query
from os import path, getcwd, chdir
from PublishingManagement import Registry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, getLogger, config
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
    #for path in sysPath:
        #print(f'{path}')
    #print(registry.search('publisher.log', 'files'))

    #log_publisher = str(registry.search('publisher.log', 'files')).lstrip('./')
    #log_publisher = str(
        #''.join(registry.report('path')
        #.get('project_root')) + '/' + str(
        #''.join(registry.search('publisher.log', 'files')))
        #.lstrip('./'))
    log_file_config = './Utilities/Maintenance/Logger.ini'
    config.fileConfig(log_file_config, disable_existing_loggers=False)
    debug('This message should appear on the console')
    info('So should this')
    warning('And this, too')
    debug('This message should go to the log file')
    info('So should this')
    warning('And this, too')
    error('And non-ASCII stuff, too, like Øresund and Malmö')

    #log_publisher = ''.join(registry.search('publisher.log', 'files'))

            #''.join(registry.report('path').get('project_root'))) + '/' \
            #+ str(directory).lstrip('./')
    #print(getcwd())
    #print(log_file_config)

    #FORMAT = '%(asctime)s %(message)s'
    #basicConfig(
        #format=FORMAT,
        #filename='log_publisher',
        #filemode='w',
        #encoding='utf-8',
        #level=INFO)
    #logger = getLogger()
    #info('[[ {} ]]\n{}>>> [ main() ]\n'
         #.format(path.basename(__file__), indent[0]))
    #info('[ project_path ]\n\t[ {} ]\n'.format(project_path))
    #info('[ project_root ]\n\t[ {} ]\n'.format(project_root))
    #info('[ test ]\n\t[ {} ]\n'.format(project_root))

    #logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='./Utilities/Data/Log/publisher.log' ,level=logging.DEBUG)
    #logger = logging.getLogger(__name__)
    #logging.debug('This message should appear on the console')
    #logging.info('So should this')
    #logging.warning('And this, too')

    #logger.debug('This message should go to the log file')
    #logger.info('So should this')
    #logger.warning('And this, too')
    #logger.error('And non-ASCII stuff, too, like Øresund and Malmö')


    #print(f'registry.search()\n  {registry.search()}\n')
    #print(f"registry.search(\'Log\')\n  {registry.search('Log')}\n")
    #print(f"registry.search(\
        #\'PublishingDirector\', \'file\')\n  \
        #{registry.search('PublishingDirector', 'file')}\n")
    #print(f"registry.search(\'.md\', \'file\')\n  \
        #{registry.search('.md', 'file')}\n")


    #print(separator.join(registry.search()))
    #print(f'registry.search(\'/Log\')\n  {registry.search('/Log')}\n')
    #print(f'registry.search()\n  {separator.join(registry.search())}\n')
    #for register, field in registry(project_root, project_name, directory_omit,
        #file_register_types).items():
        #print('{}{}:'.format(indent[1], register,))
        #for entery in field:
            #print('{}{}'.format(indent[2], entery))
        #print()
    #registry.set_sysPath()





if __name__ == "__main__":
    main()
