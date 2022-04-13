# Registry.py

from os import path, getcwd, chdir, walk
from os.path import relpath


class Registry:

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
        chdir(project_root)
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
        #return locals()


    def report(self):
        #print(self.registry)
        #for register, field in self.registry(project_root, project_name,
        #directory_omit, file_register_types).items():
        for register, field in self.registry.items():
            print('\n{}:'.format(register))
            for entery in field:
                print('  {}'.format(entery))
            print()
        #print()

#def registry_report(registry = {}):
    #for register, field in registry.items():
        #print('  {}:'.format(register,))
        #for entery in field:
            #print('    {}'.format(entery))
        #print()


    def search(self, query = 'root', dir_file = 'dir'):
        search_result = []
        if dir_file is 'dir':
            if query is 'root':
                separator = ''
                return separator.join(self.registry.get('project_root'))
            else:
                for directory in self.registry.get('project_directories'):
                    if query in directory:
                        search_result.append(directory)
                return search_result
        else:
            for register, project_files in self.registry.items():
                for entery in field:
                    if any(search_field in entery for search_field in search):
                        search_result.append(str(entery))
        return search_result