#!/bin/python

#import logging
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, getLogger, config

def main():
#log_publisher = ''.join(registry.search('publisher.log', 'files'))
            #''.join(registry.report('path').get('project_root'))) + '/' \
            #+ str(directory).lstrip('./')
    #print(getcwd())

    #FORMAT = '%(asctime)s %(message)s'
    #basicConfig(
        #format=FORMAT,
        #filename='log_publisher_file',
        #filemode='w',
        #encoding='utf-8',
        #level=INFO)
    #logger = getLogger()
    #info('[[ {} ]]\n{}>>> [ main() ]\n'
         #.format(path.basename(__file__), indent[0]))
    #info('[ project_path ]\n\t[ {} ]\n'.format(project_path))
    #info('[ project_root ]\n\t[ {} ]\n'.format(project_root))
    #info('[ test ]\n\t[ {} ]\n'.format(project_root))

    #basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='./Utilities/Data/Log/publisher.log' ,level=logging.DEBUG)
    #log_file_config = './Utilities/Maintenance/Logger.ini'

    #log_file_output_publisher = './Utilities/Data/Log/publisher.log'
    #log_file_config = './Utilities/Maintenance/Logger.yaml'
    #print(log_file_output_publisher)
    #basicConfig(filename=log_file_output_publisher, encoding='utf-8', level=DEBUG)

    #basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename=log_file_output_publisher ,level=DEBUG)
    #logger = getLogger(__name__)

    log_file_config = './Utilities/Maintenance/Logger.ini'
    config.fileConfig(log_file_config, disable_existing_loggers=False)
    debug('This message should appear on the console')
    info('So should this')
    warning('And this, too')
    debug('This message should go to the log file')
    info('So should this')
    warning('And this, too')
    error('And non-ASCII stuff, too, like Øresund and Malmö')


    #logger.debug('This message should appear on the console')
    #logger.info('So should this')
    #logger.warning('And this, too')

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
