#!/bin/python
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

#import re
#import pathlib
from pathlib import Path as libPath

#regex = r"(\w+) = (\w+|\[[^\[\]]*\])"

#test_str = ("[\"project_path = None, project_path = None, directory_omit = ['.git', '__', 'html'], file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini'], dictionary = {key0 : value, key1 : value}, tuple = (t, u, ple)\"]\n")

#matches = re.finditer(regex, test_str, re.MULTILINE)

#for matchNum, match in enumerate(matches, start=1):
    ##print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #print(f"{match.group()}")

    ##for groupNum in range(0, len(match.groups())):
        ##groupNum = groupNum + 1
        ##print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

## Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.



#filepath = pathlib.Path('.').glob('**/RegistryManager.py')
#print(dir(filepath))
#print(pathlib.PurePath(str(filepath).parts)

filepath = sorted(libPath('.').glob('**/RegistryManager.py'))
delim = '\''
#module = f"./{str(filepath).split(delim)[1]}"
module = str(filepath).split('\'')[1]
print(f"{module}")
module_name = f".{module.rsplit('/', 1)[1].strip('.py')}"
print(f"{module_name}")
module_path = module.rsplit('/', 1)[0]
print(f"{module_path}")



def test():

    clear()
    #print(section('headder'))
    #print(f"{arguments}")
    #print(section('section'))

    #color_chart_256()

    print(section('section'))
    print(f"  Project files:")
    for files in registry.report('files'):
        if '.py' in files and not '__init__.py' in files and \
            not 'InitializationManager' in files and 'RegistryManager' not \
            in files:
            print(f"    {files}")
    print(section('section'))
    print(f"  Project functions:")
    for module, functions in registry.report('functions').items():
        prefix = ''
        preferredWidth =  80
        print(f"    {module}")
        for function, arguments in functions.items():
            print(f"      {function}")
            """# I was going to load all of the project functions, but I would
            have to change how the registry stores file names, because
            machinery.SourceFileLoader(function, module).load_module()
            requires a path for the module file.  They are part of the have
            registry, but not directly associated with functions.  For them
            to be loaded with machinery, Registry.report() needs to be
            modified."""
            # machinery.SourceFileLoader(function, module).load_module()
            for argument in list(arguments):
                print(f"    {argument}")
        print()
    print(section('section'))
    print(section('footer'))


    print("\n")


    module = machinery.SourceFileLoader('color_chart_256()', './Utilities/Maintenance/Compositor.py')
    print(dir(module))
    #module.exec_module('color_chart_256')
    print(module.name)
    print(module.path)
    print(dir(module.exec_module))
    module.exec_module()
    print(module.exec_module(__name__))
    print(module.__module__)
    module.load_module()
    print()

    print(f"sysPath:")
    for paths in registry.report('sysPath'):
        print(f"  {paths}")
    print()

    module = machinery.SourceFileLoader('some_module', '/path/to/file.py').load_module()


#def assistant():
    """Testing relations."""

    registry = courier(module = 'InitializationManager',function = 'initalize')
    module = importlib.machinery.SourceFileLoader('some_module', '/path/to/file.py').load_module()
    #registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()

    invoke(".Typographer", "Utilities.Maintenance").clear()
    invoke(".UtilityManager", "Utilities.Maintenance").set_project_directory()

    headder_title = f"{project_name}, {__release__}/{__version__} :: {time_code()}"
    footer_title = f"{project_name}, {__release__}/{__version__} :: {time_code()}"

    # Headder -> Introduction.
    cprint(f"{invoke('.Typographer', 'Utilities.Maintenance').section('headder', headder_title, 'Start')}", 'green')

    # Section -> Report: arguments.
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', title = 'Report: Arguments', trace_frame = True)}")
    print(f"\nargv:\n  {argv}\n")

    # Section -> Report: Current Working Directory
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Current Working Directory', trace_frame = True)}\n")
    print(f"getcwd():\n  {getcwd()}\n")

    # Section -> Report: Initalize Registry
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Initalize Registry', trace_frame = True)}\n")
    # call initialization manager
    #print(f"initalize() registry")
    #registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()

    # Section -> Report:Functions
    #print(f"\n{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Functions', trace_frame = True)}")
    section_report_functions = courier('Typographer', 'section', "{'title' : 'Report: Functions', 'trace_frame' : 'True'}")
    print(f"{section_report_functions}")
    print()
    for module, function_list in registry.report('functions').items():
        prefix = ''
        preferredWidth =  80
        print(f"{module}")
        for function_call, arguments in function_list.items():
            print(f"  {function_call}")
            for argument in list(arguments):
                print(f"    {argument}")
        print()

    # Section -> Report: Classes
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: Classes', trace_frame = True)}")
    print()
    for classes, class_list in registry.report('classes').items():
        prefix = '  '
        preferredWidth = 80
        print(f"{classes}")
        for classes in class_list:
            postfix = ' ' * (len(str(classes).split('[')[0]) + len(str(prefix))) + '  '
            wrapper = TextWrapper(initial_indent=prefix, width=preferredWidth,
                subsequent_indent=postfix)
            message = classes
            print(wrapper.fill(message))
    print()

    # Section -> Report: Project Files
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: project_files', trace_frame = True)}")
    print()
    print(f"project_files:")
    for files in registry.report('files'):
        print(f"  {files}")
    print()

    # Section -> Report: Project Directories
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: directories', trace_frame = True)}")
    print()
    print(f"project_directories:")
    for directories in registry.report('directories'):
        print(f"  {directories}")
    print()

    # Section -> Report: sysPath
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('section', 'Report: sysPath', trace_frame = True)}")
    print()
    print(f"sysPath:")
    for paths in registry.report('sysPath'):
        print(f"  {paths}")
    print()

    # Section -> Test: Colors
    section_report_tests_checks = courier('Typographer', 'section', "{'title' : 'Tests & Checks', 'trace_frame' : 'True'}")
    print(f"{section_report_tests_checks}")
    print(f"  Color")
    courier('Compositor', 'color_chart_256')
    invoke('.Compositor', 'Utilities.Maintenance').color_chart_256()
    print()

    # Section -> Footer:  Salutation
    line_test = courier(module = 'Typographer',function = 'section', arguments = "{'subtitle' : 'TEST'}")
    print(f"{line_test}")
    print(f"Test here!!!")
    print(f"{line_test}")
    # Section -> Footer: Closing
    print(f"{invoke('.Typographer', 'Utilities.Maintenance').section('footer', footer_title, 'End')}\n")
#class courier:
  #def __init__(self):
    #self.registry = registry = invoke('.InitializationManager', 'Utilities.Maintenance').initalize()
    #self.name = name
    #self.age = age
  #def myfunc(self):
    ##print("Hello my name is " + self.name)

