#!/bin/python
# RegistryManager_01.py


from os import path, getcwd, chdir, walk
from os.path import relpath
from sys import path as sysPath
from importlib import import_module as invoke
import re




project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__


def test_function():
    test = 'test text'
    return test


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

    def __init__(
        self,
        project_root=invoke(".UtilityManager", "Utilities.Maintenance").set_project_directory(),
        project_name=project_name,
        directory_omit=None,
        file_register_types=None,
    ):
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
        # chdir(project_root)
        project_directory = project_root
        work_root = project_directory
        project_files = []
        for subdir, dirs, files in walk(project_directory):
            for filez in files:
                for file_type in file_register_types:
                    path_discovery = str(path.join(project_directory, subdir))
                    if str(filez).endswith(file_type):
                        path_relation = path.relpath(subdir, project_directory)
                        path_relation = subdir.partition(project_directory)[1:]
                        work_dir = path.basename(project_directory)
                        #path_tail = path.basename(work_root)
                        path_tail = path.basename(project_directory)
                        path_head = path_discovery.split(path_tail, 1)
                        filez_path = "." + path_head[1]
                        # filez_path = path_head[1]
                        project_files.append(str(path.join(filez_path, filez)))
        project_directories = []
        for project_directory, pdirs, pfiles in walk(project_directory):
            for subdir in pdirs:
                path_discovery = str(path.join(project_directory, subdir))
                if any(omission in path_discovery for omission in directory_omit):
                    pass
                else:
                    path_relation = path.relpath(subdir, project_directory)
                    path_relation = subdir.partition(project_directory)[1:]
                    work_dir = path.basename(project_directory)
                    path_tail = path.basename(work_root)
                    path_head = path_discovery.split(path_tail, 1)
                    project_directories.append("." + path_head[1])
                    # project_directories.append(path_head[1])
        # Find all project functions.
        regex = r"(\w+) = (\w+|\[[^\[\]]*\])"
        project_functions = {}
        for files in project_files:
            if '.py' in files:
                with open(files, 'r') as project_file:
                    files = files.split("/")[-1]
                    if 'def' in project_file.read():
                        project_functions[files] = {}
                        project_file.seek(0)
                        lines = project_file.readlines()
                        for line_number in range(0, len(lines)):
                            #current_line = lines[line_number] #.replace(':\n', '')
                            current_line = [] #.replace(':\n', '')
                            #if current_line.startswith("def "):
                            if lines[line_number].startswith("def ") and lines[line_number].endswith("(\n"):
                                parsing_lines = True
                                #next_line = 0
                                # Remove the def keyword and formate function name.
                                function_name = lines[line_number].replace('def ', '').split('(')[0] + '()'
                                project_functions[files][function_name] = []
                                while parsing_lines == True:
                                    line_number += 1
                                    if lines[line_number].endswith(",\n"):
                                        current_line = lines[line_number].lstrip().replace(',\n', '')
                                        project_functions[files][function_name].append(current_line)
                                    if lines[line_number].endswith("):\n"):
                                        current_line = lines[line_number].lstrip().replace('):\n', '')
                                        project_functions[files][function_name].append(current_line)
                                        parsing_lines = False
                            if lines[line_number].startswith("def "):
                                parsing_lines = True
                                split_name = lines[line_number].replace('def ', '').split('(')[0] + '('
                                function_name = lines[line_number].replace('def ', '').split('(')[0] + '()'
                                project_functions[files][function_name] = []
                                if lines[line_number].replace('def ', '').split(split_name)[1] == '):\n':
                                    arguments = 'None'
                                else:
                                    #arguments = lines[line_number].replace('def ', '').split(split_name)[1][:-3].split(',')
                                    arguments = lines[line_number].replace('def ', '').split(split_name)[1][:-3]
                                project_functions[files][function_name].append(arguments)
        # Find all project classes.
        project_classes = {}
        for files in project_files:
            if '.py' in files:
                with open(files, 'r') as project_file:
                    files = files.split("/")[-1]
                    if 'class ' in project_file.read():
                        project_classes[files] = []
                        project_file.seek(0)
                        lines = project_file.readlines()
                        for line_number in range(0, len(lines)):
                            current_line = lines[line_number] #.replace(':\n', '')
                            if current_line.startswith("class "):
                                finished = False
                                next_line = 0
                                while finished == False:
                                    next_line += 1
                                    if current_line.endswith("(\n"):
                                        current_line = current_line.replace('\n', '') + lines[line_number + next_line].lstrip()
                                    if current_line.endswith(",\n"):
                                        current_line = current_line.replace('\n', '') + lines[line_number + next_line].lstrip()
                                    if current_line.endswith(":\n"):
                                        current_line = current_line.replace(':\n', '')
                                        finished = True
                                current_line = current_line.replace('class ', '')
                                class_call = str(f"{current_line}")
                                project_classes[files].append(class_call)
        self.registry = {}
        self.registry = {
            'project_root': [project_root],
            'project_directories': project_directories,
            'project_files': project_files,
            'project_functions': project_functions,
            'project_classes': project_classes,
        }
        self.set_sysPath()
        # Generate registry cache files.
        self.report_cache_files()
        self.report_cache_files_appended()


    def report(self, summary='complete'):
        '''Return a specified report'''
        if summary == 'files':
            return self.registry.get('project_files')
        if summary == 'path':
            return self.registry.get('project_root')
        if summary == 'directories':
            return self.registry.get('project_directories')
        if summary == 'sysPath':
            return sysPath
        if summary == 'functions':
            return self.registry.get('project_functions')
        if summary == 'classes':
            return self.registry.get('project_classes')
        if summary == 'complete':
            return self.registry, sysPath

    def report_cache_files(self):
        """Create cache file reports.  There will be a file with entries for
        all project files, cache file with the project directories,
        there will be a file with entries of all project directories, there
        will be a file cache file with all the sysPath directories, and there
        will be a complete summary cache file which will contain all entries
        from the other lists concatinated into a single files.  This is what
        the search funcion will parse to find files, perhaps . . ."""

        # Create a dictionary of cache files, this should be made more dynamic.
        registry_cache_file = {
            'project_files': './Utilities/Data/Cache/Registry.files.cache',
            'project_root': './Utilities/Data/Cache/Registry.root.cache',
            'project_directories': './Utilities/Data/Cache/Registry.directories.cache',
            'project_sysPath': './Utilities/Data/Cache/Registry.sysPath.cache',
            #'project_functions': './Utilities/Data/Cache/Registry.functions.cache',
            #'project_classes': './Utilities/Data/Cache/Registry.classes.cache',
            'registry': './Utilities/Data/Cache/Registry.complete_summary.cache',
        }
        # The report_summaries will be sent as arguments to the report method.
        #report_summaries = ['files', 'path', 'directories', 'sysPath', 'functions', 'classes', 'summary']
        #report_summaries = ['files', 'path', 'directories', 'sysPath', 'functions', 'classes']
        report_summaries = ['files', 'path', 'directories', 'sysPath']
        registry_cache = []
        summary = 0
        # Itirate through the dictionary and on each itiration call the report.
        # Then write the results to a specified cache file.
        for report_file, report_path in registry_cache_file.items():
            if report_file not in 'registry':
                with open(registry_cache_file[report_file], 'w') as registry_cache:
                    for entry in self.report(report_summaries[summary]):
                        registry_cache.write(str(entry + '\n'))
                summary += 1  # incriment the summary key for sending to report.

        cache_files = [
            'project_root',
            'project_sysPath',
            'project_directories',
            'project_files',
            #'project_functions',
            #'project_classes',
            #'registry'
        ]
        # Now append all the files into a complete summary cache file.
        with open(registry_cache_file['registry'], 'w') as complete_summary_report:
            for files in cache_files:
                with open(registry_cache_file[files]) as partial_summary_report:
                    complete_summary_report.write(partial_summary_report.read())
        return registry_cache_file['registry']

    def report_cache_files_appended(self):
        registry_cache_file = {
            'project_functions': './Utilities/Data/Cache/Registry.functions.cache',
            'project_classes': './Utilities/Data/Cache/Registry.classes.cache',
            'registry': './Utilities/Data/Cache/Registry.complete_summary.cache',
        }
        #for files in registry_cache_file:
        with open(registry_cache_file['project_functions'], 'w') as registry_cache:
            for module, function_list in self.report('functions').items():
                registry_cache.write(str(module + '\n'))
                for function_call in function_list:
                    registry_cache.write(str(function_call + '\n'))
                #registry_cache.write(str('\n'))
        with open(registry_cache_file['project_classes'], 'w') as registry_cache:
            for module, class_list in self.report('classes').items():
                registry_cache.write(str(module + '\n'))
                for class_call in class_list:
                    registry_cache.write(str(class_call + '\n'))
                #registry_cache.write(str('\n'))
        cache_files = [
            'project_functions',
            'project_classes',
            #'registry'
        ]
        # Now append all the function and class files to the complete summary cache file.
        with open(registry_cache_file['registry'], 'a') as complete_summary_report:
            for files in cache_files:
                with open(registry_cache_file[files]) as partial_summary_report:
                    complete_summary_report.write(partial_summary_report.read())
        return registry_cache_file['registry']

    def search(self, search=None):
        """Return a search result.  This method is possibly convaluted.
        The search will scan the full summary cache file report generated by
        `self.report_cache_files()`.

        This tactic introduces a greater potential for missmatching then by
        searching through the directory paths.  However . . . since the cache
        files already exist . . . the seachable range of interest has already
        been curated.

        Damit ... I haven't even got it working yet, and somehow the sysPath
        registry is already malfunctioning.

        After analysis it has been discovered that the results of
        `self.set_sysPath()` depend on returns from `self.search()`.  So after
        changing `self.search()` `self.sysPath()` could no longer offer a
        valid return for this new implementation of `self.search()`.

        Considering that this has exposed a deficiency it was suitable to
        decide attempting a rewriting of `self.search()` with this method.

        However ... `self.sysPath()` needs to be updated first to accomodate
        the behavior of this method.
        """

        # Calling `self.report_cache_files()` will update cache files and
        # return path to summary registry file.
        # So, update and open the file.

        # That works now, just dont call `self.sysPath(True)`, it only works
        # with false, and does not depend on `self.search()`.
        search_result = []
        with open(self.report_cache_files(), 'r') as complete_summary_report:
            for line_no, line in enumerate(complete_summary_report):
                # print(line_no, line.strip())
                if search in line:
                    search_result.append(line.strip())
        return search_result

    # def set_sysPath(self, sysPath = sysPath, update_sysPath = False):
    def set_sysPath(self, update_sysPath=False):
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
        sysPath_cache_file = "./Utilities/Data/Cache/Path.cache"

        # False is the initialization state.
        if update_sysPath is False:
            # Open the cache file, give it a section headder Init,
            # and write sysPath paths to it line by line.
            with open(sysPath_cache_file, "w") as sysPath_cache:
                sysPath_cache.write(str("Init:\n"))
                for path in sysPath:
                    sysPath_cache.write(str(path + "\n"))
            # Append an append section headder and the project paths to Then
            # cache file.  Also append the project directories to sysPath.
            with open(sysPath_cache_file, "a") as sysPath_cache:
                sysPath_cache.write(str("Append:\n"))
            for directory in self.registry.get("project_directories"):
                project_path = str(self.registry.get("project_root")).lstrip(
                    "['"
                ).rstrip("']") + str(directory).lstrip(".")
                if project_path not in sysPath:
                    sysPath.append(project_path)
                    with open(sysPath_cache_file, "r+") as sysPath_cache:
                        if project_path not in sysPath_cache:
                            sysPath_cache.write(str(project_path + "\n"))
        # True is the update state.
        else:
            ## Open the cache file and get the line number for append title.
            with open(sysPath_cache_file, "r") as sysPath_cache:
                for line_no, line in enumerate(sysPath_cache):
                    if line == "Append:\n":
                        break
                # else: # for loop ended => line not found
                # line_no = -1
            # Read cache file line by line starting at the append section, and
            # remove corresponding paths from sysPath
            with open(sysPath_cache_file, "r+") as sysPath_cache:
                for count, line in enumerate(sysPath_cache):
                    if count > line_no:
                        sysPath.remove(line.strip())
            # Remove all appended paths to cache file, by overwriting it with sysPath.
            with open(sysPath_cache_file, "w") as sysPath_cache:
                sysPath_cache.write(str("Reinit:\n"))
                for path in sysPath:
                    # pass
                    sysPath_cache.write(str(path + "\n"))
            # Next ... implement some kind of update mechanism for appending new
            # paths to sysPath.
