# RegistryManager.py

from os import path, getcwd, chdir, walk
#!/bin/python


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
        #project_directory = project_root
        #work_root = project_directory
        #project_files = []
        #for subdir, dirs, files in walk(project_directory):
            #for filez in files:
                #for file_type in file_register_types:
                    #path_discovery = str(path.join(project_directory, subdir))
                    #if(str(filez).endswith(file_type)):
                        ##path_relation = path.relpath(subdir, project_directory)
                        #path_relation = subdir.partition(project_directory)[1:]
                        #work_dir = path.basename(project_directory)
                        #path_tail = path.basename(work_root)
                        #path_head = path_discovery.split(path_tail, 1)
                        #filez_path = '.' + path_head[1]
                        #project_files.append(str(path.join(filez_path, filez)))
        #project_directories = []
        #for project_directory, pdirs, pfiles in walk(project_directory):
            #for subdir in pdirs:
                #path_discovery = str(path.join(project_directory, subdir))
                #if any(omission in path_discovery for omission in
                    #directory_omit):
                    #pass
                #else:
                    #path_relation = path.relpath(subdir, project_directory)
                    #path_relation = subdir.partition(project_directory)[1:]
                    #work_dir = path.basename(project_directory)
                    #path_tail = path.basename(work_root)
                    #path_head = path_discovery.split(path_tail, 1)
                    #project_directories.append('.' + path_head[1])
        #self.registry = {'project_root':[work_root], \
            #'project_directories':project_directories,\
            #'project_files':project_files,}
        ##return locals()


    def report(self, report_file = 'path'):
        """Provides a specified report. This method still needs to be refined.


        """

        if report_file is 'console':
            for register, field in self.registry.items():
                print('\n{}:'.format(register))
                for entery in field:
                    print('  {}'.format(entery))
                print()
            return self.registry
        if report_file is 'log':
            for register, field in self.registry.items():
                #info('\n{}:'.format(register))
                for entery in field:
                    #info('  {}'.format(entery))
                    pass
                #info('')
            return self.registry
        if report_file is 'path':
            return self.registry
            return self.registry.items


    #def search(self, query = 'root', dir_file = 'directory'):
        #"""The search() method allows for serching through the registry.  More
        #explaination is needed here."""

        #search_result = []
        #if dir_file is 'directory':
            #if query is 'root':
                #separator = ''
                #return separator.join(self.registry.get('project_root'))
            #else:
                #for directory in self.registry.get('project_directories'):
                    #if query in directory:
                        #result = path.basename(directory)
                        #if query in result:
                            ##search_result.append(directory)
                            #return directory
        #else:
            #for files in self.registry.get('project_files'):
                #if query in files:
                    ##result_check = path.basename(files)
                    ##result = files
                    ##if query in result_check:
                    #search_result.append(files)
            #return search_result

    #def set_sysPath(self):
        #"""Currently this is a mess and needs to be properly implemented."""

        #print('sysPath pre-append:'.format(''))
        #for path in sysPath:
            #print('  {}'.format(path))
        #for directory in self.registry.get('project_directories'):
            #project_path = str(self.search()) + '/' \
                #+ str(directory).lstrip('./')
            #sysPath.append(project_path)
        #print('\nsysPath append:'.format(''))
        #for path in sysPath:
            #print('  {}'.format(path))
        #print('{}'.format(''))
