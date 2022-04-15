#!/bin/python

from os import path, getcwd, chdir, walk
from pathlib import Path, PurePath
from PublishingManagement import Registry
from logging import debug, info, warning, error, basicConfig, DEBUG, INFO,\
    WARNING, ERROR, CRITICAL, getLogger
import logging.config
from sys import path as sysPath
from functools import reduce

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

def pathto_dict(path_):
    for root, dirs, files in walk(path_):
        tree = {'name': root, 'type':'folder', 'children':[]}
        tree['children'].extend([pathto_dict(path.join(root, d)) for d in dirs])
        tree['children'].extend([{'name':path.join(root, f), 'type':'file'} for f in files])
        return tree

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    sep = '/'
    rootdir = rootdir.rstrip(sep)
    start = rootdir.rfind(sep) + 1
    for path, dirs, files in walk(rootdir):
        folders = path[start:].split(sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

#def getParent(str_path, levels = 1):
    #path = PurePath(str_path)
    #common = path

    ## Using for loop for getting
    ## starting point required for
    ## os.path.relpath()
    #for i in range(levels + 1):

        ## Starting point
        ##common = path.dirname(common)
        #common = Path(str_path).parent
    ## Parent directory upto specified
    ## level
    #return path.relpath(path, common)
def subfolders(path_to_parent):
     try:
        return next(walk(path_to_parent))[1]
     except StopIteration:
        return 'end'

def check_string(string, substring_list):
    for substring in substring_list:
        if substring in string:
            return False
    return True

def ExaminDirectory(registry = None):
    root_path = registry.search()
    ignore = ['.git', '_', 'objects']
    for root, dirs, files in walk(root_path):
        print(root,len(dirs))
        if not len(dirs): break


def build_tree(registry = None):
    root_path = registry.search()
    ignore = ['.git', '_', 'objects']
    print(f'root_path: {root_path}')
    for directory, sub_directory, files in walk(root_path):
        if check_string(directory, ignore):
            pass
        else:
            dir_base = directory.rsplit('/', 1)[1]
            dir_lead = directory.rsplit('/', 1)[1]
            if check_string(dir_base, ignore):
                pass
            else:
                dir_lead = directory.rsplit('/', 1)[1]
                print(f'  {dir_lead}') # prints out each directory path
                sub_directory = [n for n in sub_directory] # prints each sub folder in each dir
                sub_directory.sort() # sort subs
                #if not len(sub_directory):
                    #break
                #else:
                    #for f in sub_directory:
                        #if check_string(f, ignore):
                            #pass
                        #else:
                            #print(f'    {f}')
                print()

                #if len(dirs):
                    #print(f'  {dir_base}, {len(dirs)}')
                #if not len(dirs):
                    #print(f'  {dir_base}, {len(dirs)}')
                    ##print()
                    #break


    #print only the subs
    #for directory in registry.report('path').get('project_directories'):
    #root_path = registry.report('path').get('project_directories')
        #str = "a123"

            #if set(ignore) & set(dir_base):
                #print("ignore:", dir_base) # prints out each directory path
                #print("some of the strings found in str")
                #print("no strings found in str")
            #if '_' not in dir_base:
                #if '.git' not in dir_base:
                #print(f'  {dir_lead}') # prints out each directory path
                #print(f'  {dir_lead}\n    sub_directory: {sub_directory}') # prints out each directory path
                #print(f'  {dir_lead}\n{sub_directory}') # prints out each directory path
                #if '_' not in f:

    #for directory in registry.report('path').get('project_directories'):
        #for root, dirs, files in walk(directory):
            #if '_' not in root:
                #dir_base = root.rsplit('/', 1)[1]
        #print()



        #for dir, sub, files in walk(directory):
            #if '/_' not in dir:
                ##print('  ', dir)
                #dir_base = dir.rsplit('/', 1)[1]
                #print("", dir_base) # prints out each directory path
                #sub.sort() # sort subs
                #for f in sub:
                    #if '_' not in f:
                        #print('  ', f)
                        #if 'end' not in subfolders(f):
                            #print(subfolders(f))
                        #pass
        #print()
    #from Author import document_builder
    #document_builder(registry)
    #print(pathto_dict(registry.search('root')))
    #print(pathto_dict(registry.search('root')))
            #print()    # prints spaces between levels
        #ancestor_directory = directory.rsplit('/')[1]
        #print(directory)


        #print("************Start print********")
        #for root_dir_path, sub_dirs, files in walk(directory):
            #print("Root Directory Path: ", root_dir_path)
            #print("Sub Directories: ", sub_dirs)
            #print("Files", files)
            #print('*' * 25)


        #print only the files
        #for dir, sub, files in os.walk(my_dir):
            #print("Print Dir: ", dir) # prints out each directory path
            #sub = [n for n in sub] # prints each sub folder in each dir
            #contents = sub + files # subs and files
            #contents.sort() # sorst subs and files

            #for f in contents:
                #if os.path.isfile(f):
                    #print('\tJust The Files', f)
            #print()    # prints spaces between levels

        #print only the subs
            #print("Print Dir: ", dir) # prints out each directory path
                #print("", dir) # prints out each directory path
            #sub = [n for n in sub] # prints each sub folder in each dir
                #print('\tJust The Subs', f)
                #if 'html' not in f:
                #if not f.startswith("_"):

        #print("************End print********")
        #print(getParent(directory))
        #print(pathto_dict(directory))
        #print(get_directory_structure(directory))
        #for key, value in get_directory_structure(directory).items():
            #print(f'  {key}:\n{value}\n')
            #for xkey, xvalue in pathto_dict(directory).get(key):
                #print(f'  {xkey}:\n{xvalue}\n')

    #for directory in registry.report('path').get('project_directories'):
        ##ancestor_directory = directory.rsplit('/')[1]
        #print(directory)
        ##print(pathto_dict(directory))
        #for key, value in pathto_dict(directory).items():
            #print(f'  {key}:{value}')
            #for xkey, xvalue in pathto_dict(directory).get(key):
                #print(f'  {xkey}:{xvalue}')
            #print(pathto_dict('children'))
            #print(pathto_dict(directory))
            #for dirs in root:
                #print(pathto_dict(directory))
                #for files in root:
                    #print(pathto_dict('children'))



        #if ancestor_directory != '.':
            ##parent_directory = directory.split('./', 1)[1].split('/', 1)[0]
            #parent_directory = ancestor_directory.rsplit('/')[0]
            #print(f'parent {parent_directory}')

        ##ancestor_directory = directory.split('/')[0]
        ##parent_directory = ancestor_directory.split('./')[1].split('/')[0]
        #descendant_directory = directory.split('/', 1)[1]


        #print(directory)
        #print(ancestor_directory)
        #print(descendant_directory)
        #print(f'{ancestor_directory}::{parent_directory}::{descendant_directory}')
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

    #log_register(registry, log_director)
    #build_tree(registry)
    #ExaminDirectory(registry)
    #registry.report()
    #for paths, directories in registry.report('path').items():
    rst_tree_repository = './Administration/Athenaeum/Publisher/Composer/Author/tree'
    for paths in registry.report('path').get('project_directories'):
        #for pathz in directories:
            #print(pathz)
        #print(paths)
        paths = paths[2:].split('/')
        #print(paths)
        for path in paths:
            if check_string(path, '_'):
                #print(path)
                rst_tree_path = rst_tree_repository + '/' + path + '.rst'
                print(rst_tree_path)
                #check_path = path.join(rst_tree_path)
                #if not path.exists(check_path):

                if Path(rst_tree_path).is_file():
                    print ("File exist")
                else:
                    print ("File not exist - make it.")
                    rst_file = open(rst_tree_path, 'w').close()
                    #f = open("myfile.txt", "x")







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
