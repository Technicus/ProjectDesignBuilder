#!/bin/python

from os import chdir, getcwd, listdir, remove
from os.path import exists as file_exists

def count_substring(string, sub_string):
    count = 0
    for i, j in enumerate(string):
        if sub_string in string[i:i+1]:
            count = count + 1
    return count

def reset_files(rem_path = None, ext = None):
    for file_name in listdir(rem_path):
        if file_name.endswith(ext):
            remove(rem_path + file_name)

def build_path_documentation_tree(registry = None, rst_tree_repository = None):

    registry_path_report = registry

    # Create root project document and insert headding
    project_name = 'ProjectDesignBuilder'
    reset_files(rem_path = rst_tree_repository + '/', ext = '.rst')
    rst_tree_repository_file_project = rst_tree_repository + '/' + project_name + '.rst'
    with open(rst_tree_repository_file_project, 'w') as rst_file:
        rst_file.write(f".. _{project_name}:\n\n")
        rst_file.write(f"{project_name}\n")
        rst_file.write(f"{'=' * len(project_name)}\n\n")




    path_counter = 0
    for relative_path in registry_path_report:
        path_split = relative_path.split('/', count_substring(relative_path, '/'))
        path_splits = count_substring(relative_path, '/')
        path_counts = len(relative_path.split('/', count_substring(relative_path, '/')))

        print(f"path_split = {path_split}")
        print(f"path_splits = {path_splits}")
        print(f"path_counts = {path_counts}")

        # Create rst files for root project directories
        # start with first index
        if path_splits == 1:
            # Loop through path branches and make entries in project rst file
            for branches in range(1, path_counts):
                rst_file = open(rst_tree_repository_file_project, "r+")
                rst_file_read = rst_file.read()
                if path_split[branches] in rst_file_read:
                    print(f"{path_split[branches]} is in {rst_file.name}.")
                    pass
                else:
                    rst_file.write(f'{path_split[branches]}\n')
                rst_file.close()
                # Also create root directory branch rst files.
                if file_exists(rst_tree_repository + '/' + path_split[branches] + '.rst'):
                    print(f"{path_split[branches] + '.rst'} exists")
                else:
                    print(f"{path_split[branches] + '.rst'} no exist, create it.")
                    with open(rst_tree_repository + '/' + path_split[branches] + '.rst', 'w') as rst_file:
                        rst_file.write(f'{path_split[branches]}\n')
        else:
            # Advance to next level of branches, and itirate through each list.
            # Open root rst file from range 1, then append range 2
            # Then create a new rst file for next range, and append next range.
            for branches in range(1, path_counts):
                # If the file exists, open and append to it, else create a new one.
                if file_exists(rst_tree_repository + '/' + path_split[branches] + '.rst'):
                    print(f"{path_split[branches] + '.rst'} exists, {path_split[branches]} will be appended.")
                    # Check to find if path_split[branches + 1] is already in file.
                    rst_file = open(rst_tree_repository + '/' + path_split[branches] + '.rst', "r+")
                    rst_file_read = rst_file.read()
                    if branches + 1 < len(path_split):
                        if path_split[branches + 1] in rst_file_read:
                            print(f"{path_split[branches + 1]} is in {rst_file.name}.")
                            rst_file.close()
                        else:
                            with open(rst_tree_repository + '/' + path_split[branches] + '.rst', 'a') as rst_file:
                                rst_file.write(f'{path_split[branches + 1]}\n')
                else:
                    print(f"{path_split[branches] + '.rst'} no exists, {path_split[branches]} will be manufactured.")
                    with open(rst_tree_repository + '/' + path_split[branches] + '.rst', 'a') as rst_file:
                        rst_file.write(f'{path_split[branches]}\n')

        #print(f"{relative_path.split('/', count_substring(relative_path, '/'))}")
        #print(f"{count_substring(relative_path, '/')}")
        #print(f"{len(relative_path.split('/', count_substring(relative_path, '/')))}")

        #for branches in range(0, path_counts):
            #print(f"path_split[{branches}] = {path_split[branches]}")
            ##print(f"{branches}")
            ##for branches in path_split:
            #if path_split[branches] == '.':
                ##print(f"{path_split[branches + 1]} is in project root.")
                ##rst_tree_repository_file = rst_tree_repository + '/' + path_split[1] + '.rst'
                ##if path_split[1] in open(rst_tree_repository_file_project, 'r') as rst_file:
                ## opening a text file
                #rst_file = open(rst_tree_repository_file_project, "r+")
                ## read file content
                #rst_file_read = rst_file.read()
                #if path_split[branches + 1] in rst_file_read:
                    #print(f"{path_split[branches + 1]} is in {rst_file.name}.")
                    #pass
                ##close()
                #else:
                    ##with open(rst_tree_repository_file_project, 'a') as rst_file:
                    #rst_file.write(f'{path_split[branches + 1]}\n')
                ## closing a file
                #rst_file.close()


            ## check if branch rst file exists.
            #if path_split[branches] != '.':
                #if file_exists(rst_tree_repository + '/' + path_split[branches] + '.rst'):
                    #print(f"{path_split[branches] + '.rst'} exists")
                    #rst_file = open(rst_tree_repository + '/' + path_split[branches] + '.rst', "r+")
                    #if path_split[branches - 1] == '.':
                        #print("can not be '..rst'")
                        #parent = False
                    #else:
                        #rst_file_parent = open(rst_tree_repository + '/' + path_split[branches - 1] + '.rst', "r+")
                        #parent = True
                    ## read file content
                    #rst_file_read = rst_file.read()
                    #if parent is True:
                        #rst_file_read_parent = rst_file_parent.read()
                    #if path_split[branches] in rst_file_read:
                        #print(f"{path_split[branches]} is in {rst_file.name}.")
                        ##print(f"len(path_split[{branches}]) = {len(path_split[branches])}")
                        ##rst_file.write(f'{path_split[branches]}\n')
                        ## Append next branch to file.
                        ##compare_branch_len = int(len(path_split[branches])) + 1
                        ##compare_split_len = int(len(path_split[branches]))
                        ##if compare_branch_len < compare_split_len:
                            ##print(f"{path_split[branches + 1]} append to {rst_file.name}.")
                            ##rst_file.write(f'{path_split[branches + 1 ]}\n')
                    #else:
                        #print(f"Write {path_split[branches]} to {rst_file.name}.")
                        ##with open(rst_tree_repository_file_project, 'a') as rst_file:
                        #rst_file.write(f'{path_split[branches]}\n')

                    #if parent is True:
                        #if path_split[branches] in rst_file_read_parent:
                            #print(f"{path_split[branches]} is in {rst_file_parent.name}.")
                        #else:
                            #if path_split[branches] in rst_file_read_parent:
                                #print(f"{path_split[branches]} is in {rst_file_parent.name}.")
                            #else:
                                #print(f"Write {path_split[branches]} to {rst_file_parent.name}.")
                                ##with open(rst_tree_repository_file_project, 'a') as rst_file:
                                #rst_file_parent.write(f'{path_split[branches]}\n')

                    ## closing a file
                    #rst_file.close()
                    #if parent is True:
                        #rst_file_parent.close()
                #else:
                    #print(f"{path_split[branches] + '.rst'} not exist, make it.")
                    #with open(rst_tree_repository + '/' + path_split[branches] + '.rst', 'a') as rst_file:
                        #rst_file.write(f'{path_split[branches]}\n')
                ##rst_file = open(path_split[branches], "r+")



        print()

def main():
    #rst_tree_repository_file = rst_tree_repository + '/' +'test.file'
    #with open(rst_tree_repository_file, 'w') as rst_file:
        #rst_file.write(f'{getcwd()}\n')
    #project_directories = registry.report('path').get('project_directories')
    #project_root = ','.join(registry.report('path').get('project_root')) + '/'
    #rst_tree_repository = './Administration/Athenaeum/Publisher/Composer/Author/tree'

    chdir('../')
    rst_tree_repository = './Test/rst'
    registry = ['./Administration', './Builder', './Design', './Composition', './Utilities', './Administration/Legal', './Administration/Guides', './Administration/Tutorial', './Administration/Athenaeum', './Administration/Athenaeum/Documentum', './Administration/Athenaeum/Publisher', './Administration/Athenaeum/Documentum/Proscribo', './Administration/Athenaeum/Publisher/Director', './Administration/Athenaeum/Publisher/Composer', './Administration/Athenaeum/Publisher/Composer/Author', './Administration/Athenaeum/Publisher/Composer/Editors', './Administration/Athenaeum/Publisher/Composer/Reports', './Administration/Athenaeum/Publisher/Composer/Author/tree', './Builder/Directors', './Builder/Operators', './Builder/Directors/Parameters', './Builder/Operators/Inspectors', './Builder/Operators/Designers', './Builder/Operators/Constructors', './Design/Assemblies', './Design/Drawings', './Design/Resources', './Design/Resources/Library', './Design/Resources/Models', './Design/Resources/Templates', './Design/Resources/Assets', './Design/Resources/Media', './Design/Resources/Examples', './Design/Resources/Media/Images', './Design/Resources/Media/Video', './Design/Resources/Media/Presentations', './Design/Resources/Media/Images/CoverPage', './Composition/Revisors', './Composition/Sandbox', './Composition/Exporters', './Composition/Validators', './Composition/Releases', './Composition/Sandbox/Room', './Composition/Sandbox/Assembly', './Composition/Sandbox/Box', './Composition/Sandbox/Models', './Utilities/Data', './Utilities/Maintenance', './Utilities/Configuration', './Utilities/Data/Log', './Utilities/Data/Cache', './Utilities/Data/Cache/Registry']

    build_path_documentation_tree(registry, rst_tree_repository)


if __name__ == "__main__":
    main()



#if Path(rst_tree_path).is_file():
            ##path.exists(rst_tree_path):
            #print(f'exist - open')
        #else:
            #print(f'no exist - create & open')
            ##print (f'{path} append to file.')
            #with open(rst_tree_path, 'a+') as rst_file:
                #print(f'Write rst_tree_path{rst_tree_path} to file')
                #rst_file.write(f'{rst_tree_path}\n')
                ##check_path = path.join(rst_tree_path)
