#!/bin/python
#ProjectEvaluation.py


def process_inspection(argumentation = None):
    """Returns process information that can be implemanted into
    _section() to help with diagnostics.  This function needs
    some refinement to return specific information."""

    line_number = str(currentframe().f_back.f_lineno)
    arguments_caller = str(currentframe().f_back.f_locals)
    arguments_local = str(currentframe().f_locals)
    inspection = str(currentframe().f_back.f_code)
    inspection = inspection.split(',')
    inspection[0] = inspection[0].split(' ')[2]
    inspection[1] = inspection[1].split('/')[-1].replace('\"', '')
    inspection[2] = inspection[2].split(' ')[-1].replace('>', '')
    inspection.append(inspection[0])
    inspection[0] = inspection[1]
    inspection[1] = inspection[3]
    inspection[3] = line_number
    evaluation = {}
    evaluation['file'] =  inspection[0]
    evaluation['call'] =  inspection[1]
    evaluation['function'] =  inspection[2]
    evaluation['process line'] =  inspection[3]
    evaluation['call arguments'] =  literal_eval(arguments_caller)
    evaluation['current arguments'] =  literal_eval(arguments_local)
    call_file = evaluation['call arguments']['argv'][0]
    call_line = str(getline('./' + call_file, int(evaluation['process line']))).strip()
    evaluation['call line'] = call_line

    return evaluation


def _section(marker = None):
    """This funciton returns a section for printing to console or adding
    to logs to seperate process for improving readability.  It also
    provides some process information.  This can be improved with more
    development of process_inspection()."""

    if marker is None:
        marker = '='
    terminal_size = get_terminal_size()
    working_file = __file__.split('/')
    line_number = str(currentframe().f_back.f_lineno)
    section = '\n[ ' + working_file[-1] + ' ] : ' + '( ' + line_number + ' )' + \
        marker * (terminal_size.columns - len(line_number) - \
        len(working_file[-1]) - 11 )

    return section


def review(registry = None):
    """This function will print some status information to the console. It is
    a diagnostic function."""

    # Verify the registry memory location.
    print(f"{_section('-')}")
    print(f"\nregistry = {registry}")
    # Display the properties and methosed for registry object.
    print(f"{_section('-')}")
    print(f"\nproperty_and_method for registry:")
    for property_and_method in dir(registry):
        if property_and_method.find('__'):
            print(f"  {property_and_method}")
    # Print the Root directory report.
    print(f"{_section('-')}")
    for value in registry.report()[0].get('project_root'):
        print(f"  {value}")
    print(f"{_section('-')}")
    # Print the Project Directories report.
    for value in registry.report()[0].get('project_directories'):
        print(f"  {value}")
    print(f"{_section('-')}")
    # Print the Project Files report.
    for value in registry.report()[0].get('project_files'):
        print(f"  {value}")
    print(f"{_section('-')}")
    # Print the Project sysPath report.
    print(f"\nregistry.report()[1]: sysPath")
    for register in registry.report()[1]:
        print(f"  {register}")
    print(f"{_section()}\n")

    return None


def evaluation(registry = None):
    print(f"{_section()}")
    #print(f"registry.search('Map') = {registry.search('Map', dir_file = 'directory')}")
    #print(f"registry.search('ProjectDesignBuilder.mm') = {registry.search('ProjectDesignBuilder.mm', dir_file = 'file')}")

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

    ## Report to console: path to 'RegistryManager.py'.
    #registry_manager_path = find_file(getcwd(), 'RegistryManager.py')
    #registry_manager_path = registry_manager_path.replace(getcwd(), '')
    #registry_manager_path = registry_manager_path.replace('/', '.').split('.', 1)[1]
    #registry_manager_path = registry_manager_path.rsplit('.', 1)[0]

    #print(find_file(getcwd(), 'Registry.files.cache'))
    #cache_path = find_file(getcwd(), 'Registry.files.cache')
    #cache_path = cache_path.replace(getcwd(), '.')
    #cache_path = cache_path.rsplit('/', 1)[0]
    #print(cache_path)

    return None