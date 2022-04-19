#!/bin/python
# RegistryManager_01.py


from os import path, getcwd, chdir, walk
from os.path import relpath
from sys import path as sysPath

class Registry:
    """Registry class will track all files and directories within the
    path of a project root directory.  It has methods for searching through
    the registry, for providing reports, and adding the registry paths to
    python system path.

    :param project_root: An absolute path to the project root.
    :type project_root: str
    :class:`Registry`
    :param project_name: Name of project.
    :type project_name: str"""

    def __init__(self, project_root=None, project_name=None, \
                 directory_omit=None, file_register_types=None):
        if project_root is None:
            self.project_root = getcwd()
        else:
            self.project_root = project_root
        if directory_omit is None:
            self.directory_omit = []
        else:
            self.directory_omit = directory_omit
        if file_register_types is None:
            self.file_register_types = []
        else:
            self.file_register_types = file_register_types
        """Return a list of files and a list of directories.
            This function will identify necessary path information.  Then
            also change current working directory to absolute path of
            project root."""
        #chdir(project_root)
        project_directory = project_root
        work_root = project_directory
        project_files = []
        for subdir, dirs, files in walk(project_directory):
            for filez in files:
                for file_type in file_register_types:
                    path_discovery = str(path.join(project_directory, subdir))
                    if(str(filez).endswith(file_type)):
                        path_relation = path.relpath(subdir, project_directory)
                        path_relation = subdir.partition(project_directory)[1:]
                        work_dir = path.basename(project_directory)
                        path_tail = path.basename(work_root)
                        path_head = path_discovery.split(path_tail, 1)
                        filez_path = '.' + path_head[1]
                        project_files.append(str(path.join(filez_path, filez)))
        project_directories = []
        for project_directory, pdirs, pfiles in walk(project_directory):
            for subdir in pdirs:
                path_discovery = str(path.join(project_directory, subdir))
                if any(omission in path_discovery for omission in
                    directory_omit):
                    pass
                else:
                    path_relation = path.relpath(subdir, project_directory)
                    path_relation = subdir.partition(project_directory)[1:]
                    work_dir = path.basename(project_directory)
                    path_tail = path.basename(work_root)
                    path_head = path_discovery.split(path_tail, 1)
                    project_directories.append('.' + path_head[1])
        self.registry = {'project_root':[work_root], \
            'project_directories':project_directories,\
            'project_files':project_files,}
        self.set_sysPath()
        #return locals()


    def report(self, summary = 'complete'):
        """Return a specified report"""
        if summary == 'complete':
            return self.registry, sysPath
        if summary == 'files':
            return self.registry.get('project_files')
        if summary == 'directories':
            return self.registry.get('project_directories')
        if summary == 'path':
            return self.registry.get('project_root')
        if summary == 'sysPath':
            return sysPath

    def search(self, query = 'root', dir_file = 'directory'):
        """Return a search result"""
        search_result = []
        if dir_file == 'directory':
            if query == 'root':
                separator = ''
                return separator.join(self.registry.get('project_root'))
            else:
                for directory in self.registry.get('project_directories'):
                    if query in directory:
                        result = path.basename(directory)
                        if query in result:
                            #search_result.append(directory)
                            return directory
        else:
            for files in self.registry.get('project_files'):
                if query in files:
                    #result_check = path.basename(files)
                    #result = files
                    #if query in result_check:
                    search_result.append(files)
            return search_result

    #def set_sysPath(self, sysPath = sysPath, update_sysPath = False):
    def set_sysPath(self, update_sysPath = False):
        """Append project directories to python path.
         This method will have two states:
          -- appending to the sysPath object during the registry initialization,
          -- updating the sysPath object after having been appended

          When the method appends to the sysPath object it also creates a cache
          file and writes the initial sysPath paths to it line by line.

          It also writes the appended paths to the file.

          The cache file is overwritten at each initalization.
          """

        # The sysPath_cache file will eventually be dynamically assigned,
        # by searching the path for specified cache file.
        sysPath_cache = []
        sysPath_cache_file = './Utilities/Data/Cache/Registry.sysPath.cache'

        # False is the initialization state.
        if update_sysPath is False:
            # Open the cache file, give it a section headder Init,
            # and write sysPath paths to it line by line.
            with open(sysPath_cache_file, 'w') as sysPath_cache:
                sysPath_cache.write(str('Init:\n'))
                for path in sysPath:
                    sysPath_cache.write(str(path + '\n'))
            # Append an append section headder and the project paths to Then
            # cache file.  Also append the project directories to sysPath.
            with open(sysPath_cache_file, 'a') as sysPath_cache:
                sysPath_cache.write(str('Append:\n'))
            for directory in self.registry.get('project_directories'):
                project_path = str(self.search()) + '/' \
                    + str(directory).lstrip('./')
                if project_path not in sysPath:
                    sysPath.append(project_path)
                    with open(sysPath_cache_file, 'r+') as sysPath_cache:
                        if project_path not in sysPath_cache:
                            sysPath_cache.write(str(project_path + '\n'))
        # True is the update state.
        else:
            # Open the cache file and get the line number for append title.
            with open(sysPath_cache_file, 'r') as sysPath_cache:
                for line_no, line in enumerate(sysPath_cache):
                    if line == 'Append:\n':
                        break
                #else: # for loop ended => line not found
                    #line_no = -1
            # Read cache file line by line starting at the append section, and
            # remove corresponding paths from sysPath
            with open(sysPath_cache_file, 'r+') as sysPath_cache:
                for count, line in enumerate(sysPath_cache):
                    if count > line_no:
                        sysPath.remove(line.strip())
            # Remove all appended paths to cache file, by overwriting it with sysPath.
            with open(sysPath_cache_file, 'w') as sysPath_cache:
                sysPath_cache.write(str('Reinit:\n'))
                for path in sysPath:
                    sysPath_cache.write(str(path + '\n'))
            # Next ... implement some kind of update mechanism for appending new
            # paths to sysPath.
