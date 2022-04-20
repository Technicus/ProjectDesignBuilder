#!/bin/python
#ProjectEvaluation.py

def evaluate(argv)


    # Change the current working directory to file directory.
    project_name = 'ProjectDesignBuilder'
    project_root = set_current_working_directory()
    project_path = project_root[0] + project_name

    # Report to console: path to 'RegistryManager.py'.
    registry_manager_path = find_file(getcwd(), 'RegistryManager_01.py')
    registry_manager_path = registry_manager_path.replace(getcwd(), '')
    registry_manager_path = registry_manager_path.replace('/', '.').split('.', 1)[1]
    registry_manager_path = registry_manager_path.rsplit('.', 1)[0]

    # Establish argument variables to create registry
    directory_omit = ['.git', '__', 'html']
    file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']

    # Create a registery.
    registry = import_module(registry_manager_path).Registry(project_root,
        project_name, directory_omit, file_register_types)

    #for property_and_method in dir(registry):
        #if property_and_method.find('__'):
            #print(f"  {property_and_method}")

    #for register, listing in registry.report()[0].items():
        #print(f"\n{register}:")
        #for value in listing:
            #print(f"  {value}")
        #print(f"{_section('-')}")

    ##print(f"{_section('-')}")
    #print(f"\nregistry.report()[1]")
    #for register in registry.report()[1]:
        #print(f"  {register}")

    # Test section
    ''' Search test '''
    #print(registry.report('sysPath'))
    #registry.report_cache_files()
    print(f"\nregistry.search():{''}")
    for query in registry.search('Administration'):
        print(f"  {query}")
    #registry.set_sysPath(True)
    #print(registry.report('sysPath'))
    #Registry set_sysPath() test.
    #registry.set_sysPath(update_sysPath = True)
    ##for path in registry.report('sysPath'):
    #for path in registry.report('sysPath'):
        #print(f"  {path}")
    print(f"{_section()}\n")


def evaluate(argv)
    # Report to console: file name and current function with arguments.
    print(f"{_section()}\n")
    print(f"__file__.split('/')[-1] : __name__.split('__')[1](argv[1:])")
    print(f"{__file__.split('/')[-1]} : {__name__.split('__')[1]}({argv[1:]})")

    # Report to console: current working directory.
    print(f"{_section('-')}")
    print(f"\ngetcwd()")
    print(f"{getcwd()}")

    # Change the current working directory to file directory.
    print(f"{_section('-')}")
    project_name = 'ProjectDesignBuilder'
    project_root = set_current_working_directory()
    project_path = project_root[0] + project_name
    print(f"\nproject_name = {project_name}")
    print(f"set_current_working_directory()")
    print(f"project_path = set_current_working_directory()")
    print(f"{project_path}")

    # Report to console: current working directory.
    print(f"{_section('-')}")
    print(f"\ngetcwd()")
    print(f"{getcwd()}")

    # Report to console: path to 'RegistryManager.py'.
    print(f"{_section('-')}\n")
    registry_manager_path = find_file(getcwd(), 'RegistryManager_01.py')
    registry_manager_path = registry_manager_path.replace(getcwd(), '')
    registry_manager_path = registry_manager_path.replace('/', '.').split('.', 1)[1]
    registry_manager_path = registry_manager_path.rsplit('.', 1)[0]
    print(f"{registry_manager_path}")

    # Establish argument variables to create registry
    print(f"{_section('-')}")
    #project_path = getcwd().split(project_name)
    #project_root = project_path[0] + project_name
    directory_omit = ['.git', '__', 'html']
    file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini']
    print(f"\ndirectory_omit = {directory_omit}")
    print(f"file_register_types = {file_register_types}")
    print(f"project_path = {project_path}")
    print(f"project_root = {project_root}")

    # Create a registery.
    print(f"{_section('-')}")
    print(f"\nCreate registry.")
    #registry = import_module('Utilities.Data.Program.RegistryManager_01').Registry()
    registry = import_module(registry_manager_path).Registry(project_root,
        project_name, directory_omit, file_register_types)

    print(f"{_section('-')}")
    print(f"\nregistry = {registry}")

    print(f"{_section('-')}")
    print(f"\nproperty_and_method for registry:")
    for property_and_method in dir(registry):
        if property_and_method.find('__'):
            print(f"  {property_and_method}")

    print(f"{_section('-')}")
    #print(f"registry.report()[0].items()")
    for register, listing in registry.report()[0].items():
        print(f"\n{register}:")
        for value in listing:
            print(f"  {value}")
        print(f"{_section('-')}")

    #print(f"{_section('-')}")
    print(f"\nregistry.report()[1]")
    for register in registry.report()[1]:
        print(f"  {register}")

    ## Print base registry reports.
    #for register, listing in registry.report()[0].items():
        #print(f"\n{register}:")
        #for value in listing:
            #print(f"  {value}")
        #print(f"{_section('-')}")

    print(f"{_section('-')}")
    #print(f"registry.search('Map') = {registry.search('Map', dir_file = 'directory')}")
    #print(f"registry.search('ProjectDesignBuilder.mm') = {registry.search('ProjectDesignBuilder.mm', dir_file = 'file')}")
    print(f"{_section()}\n")

    # Test section
    ''' Search test '''
    #print(registry.report('sysPath'))
    #registry.report_cache_files()
    print(f"\nregistry.search():{''}")
    for query in registry.search('Administration'):
        print(f"  {query}")
    #registry.set_sysPath(True)
    #print(registry.report('sysPath'))
    #Registry set_sysPath() test.
    #registry.set_sysPath(update_sysPath = True)
    ##for path in registry.report('sysPath'):
    #for path in registry.report('sysPath'):
        #print(f"  {path}")
    print(f"{_section()}\n")

