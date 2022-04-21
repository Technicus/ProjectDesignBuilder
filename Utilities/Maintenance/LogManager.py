# 2022.04.20.21.57


from os import getcwd, chdir, walk, scandir, listdir, remove
from os import path as osPath
from pathlib import Path, PurePath
from PublishingManagement import Registry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, CRITICAL, getLogger
import logging.config
from sys import path as sysPath
from functools import reduce
from glob import glob as glob # just because
#from os import path


def log_register(registry = None, logger = None):
    logger.info(registry)
    logger.info(registry.search())
    logger.info(registry.report())
    logger.info(sysPath)
    logger.info(logger)



# Setup an configure logging from config file.
log_file_config = registry.search(query = 'Logger_Documentum.ini', dir_file = 'file')
logging.config.fileConfig(log_file_config)
log_director = getLogger('Director')
