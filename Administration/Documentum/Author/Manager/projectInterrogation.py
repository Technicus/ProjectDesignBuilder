#!/bin/python

from sys import path as sysPath, executable
from os import system, path, getcwd, chdir, scandir, listdir, walk
from os.path import relpath
import subprocess
#from collections import defaultdict
#import logging


def projectDirectory(projectRoot = 'none'):
    """This function will identify necessary path information.  Then
        also change current working directory to absolute path of
        project root."""
    head_tail = getcwd().split(projectRoot)
    projectRoot = head_tail[0] + projectRoot
    chdir(projectRoot)
    #del(projectRoot)
    del(head_tail)
    return locals()


def projectRegister():
    """This function will generate and return a project registry.
        All paths are relative to current directory.
        The register is a dictionary of dictinaries which are:
            'projectFiles_MD'          dictionary of *.md files
            'projectFiles_PY'          dictionary of *.py files
            'projectFiles_RST'         dictionary of *.rst files
            'projectFiles_HTML'        dictionary of *.html files
            'projectDirectoriess'      dictionary of all directories
    """
    #directories = []
    #files = []
    #with scandir() as pathReview:
        #for audit in pathReview:
            #if not audit.name.startswith('.') and audit.is_dir():
                #directories.append(audit.name)
    #with scandir() as pathReview:
        #for audit in pathReview:
            #if not audit.name.startswith('.') and audit.is_file():
                #files.append(audit.name)
    #del(audit)
    #del(pathReview)
    #return locals()


#def directorySurvey(directory = getcwd()):
    """directorySurvey will conduct the work of finding information within a directory."""
    #print('[[ DirectoryDiscovery.py :: directorySurvey() ]]\n')
    directories = []
    files = []
    #print('Survey path:\n{}\n'.format(directory))
    with scandir() as pathReview:
        #print('Directories:')
        for audit in pathReview:
            #if not audit.name.startswith('.') and audit.is_file():
            if not audit.name.startswith('.') and audit.is_dir():
                #print('  {}'.format(audit.name))
                directories.append(audit.name)
        #print('Files:')
    with scandir() as pathReview:
        for audit in pathReview:
            if not audit.name.startswith('.') and audit.is_file():
                #print('  {}'.format(audit.name))
                files.append(audit.name)

    #for address in projectTreeRegister()['rootBranch']:
        #sysPath.append(address)
    subdirs = [x[0] for x in walk(getcwd())]
    for dirz in subdirs:
        if '.git' not in dirz:
            #subdirs.remove(subdirs(filez))
            #print(dirz)
            directories.append(dirz)

    del(audit)
    del(pathReview)
    #del(directory)
    #print('\nLocals():')
    #for key, value in locals().items():
        #print('{} : {}'.format(key, value))
    #print('')
    #print('{}\n'.format(locals()))
    return locals()



def sysPathAppend(report = False):
    if(report == True):
        indent = ['', '  ', '    ', '        ']
        print('{}>>> sysPath appending:\n'.format(indent[0]))
        print('{}sysPath pre-append:'.format(indent[1]))
        for address in sysPath:
            print('{}{}'.format(indent[2], address))

    #for address in projectTreeRegister()['rootBranch']:
        #sysPath.append(address)
    subdirs = [x[0] for x in walk(projectRoot)]
    for dirz in subdirs:
        if '.git' not in dirz: # subdirs.remove(subdirs(filez))
            #print(dirz)
            sysPath.append(dirz)

    if(report == True):
        print('\n{}sysPath post-append:'.format(indent[1]))
        for address in sysPath:
          print('{}{}'.format(indent[2], address))
        print('{}'.format(indent[0]))



def subprocessManagement():
    """Subprocesses"""
    # -- Append sysPath -----------------------------------------------------

    sysPathAppend(report = True)

    #test = spawn_python_script('./test.py')
    python_path = ":".join(sysPath)[1:] # strip leading colon
    #return subprocess.Popen(params, env={'PYTHONPATH':python_path}, shell=False, start_new_session = True) #, CREATE_NEW_CONSOLE = True)
    #test = subprocess.call('./test.py', env={'PYTHONPATH':python_path}, shell=True) #, start_new_session = True) #, CREATE_NEW_CONSOLE = True)

    subProcessTest = subprocess.run('./test.py', stdin=None, input=None, stdout=None, stderr=None,
                          capture_output=True, shell=True, cwd=None, timeout=None,
                          check=False, encoding=None, errors=None, text=None, env={'PYTHONPATH':python_path},
                          universal_newlines=None)

    #for returns in subProcessTest():
        #print('{}{}'.format(indent[2], subProcessTest))
    ##print('{}{}\n'.format(indent[2], test))
    #print('{}'.format(indent[0]))

    #test = subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None,
                          #capture_output=False, shell=False, cwd=None, timeout=None,
                          #check=False, encoding=None, errors=None, text=None, env=None,
                          #universal_newlines=None, **other_popen_kwargs)
    #test.kill()

def report(subject = '', printReport = False):
    indent = ['', '  ', '    ', '        ']
# -- Report directoryComprehension() -----------------------------------------------------
    if(subject == 'directoryComprehension'):
        if(printReport == True):
            print('{}>>> directoryComprehension():\n'.format(indent[0]))
            for directory, address in directoryComprehension(project).items():
                print('{}{}:\n{}{}\n'.format(indent[1], directory, indent[2], address))
            print('{}rootBranch:'.format(indent[1]))
            for audit in directorySurvey(directoryComprehension(project)['dirProjectDesignBuilder_Absolute'])['directories']:
                print('{}{}'.format(indent[2], audit))
            print('{}'.format(indent[0]))
        else:
            return(directorySurvey(directoryComprehension(project)['dirProjectDesignBuilder_Absolute']))

# -- Project registry tree  -----------------------------------------------------
    if(subject == 'registryTree'):
        if(printReport == True):
            print('{}>>> Project registry tree:\n'.format(indent[0]))

            for key, registry in projectTreeRegister().items():
                print('{}{}:'.format(indent[1], key))
                for register in projectTreeRegister()[key]:
                    print('{}{}'.format(indent[2], register))
                print('{}'.format(indent[0]))
            #del(key)
            #del(register)
            #del(subject)
            #del(returns)
            #del(indent)
            #return locals()
            return projectTreeRegister()
        else:
            return projectTreeRegister()

        #del(rootBranch)
        #print('{} : {}'.format(key, value))
        #print(projectTreeRegister())
        #print()

    if(subject == 'sysPath'):
        if(printReport == True):
            print('{}>>> sysPath:\n'.format(indent[0]))
            print('{}sysPath post-append:'.format(indent[1]))
            for address in sysPath:
                print('{}{}'.format(indent[2], address))
            print('{}'.format(indent[0]))
            return sysPath
        else:
            return sysPath



def projectTreeRegister(projectDirectory = getcwd(), fileTypes = ('.md', '.py', '.rst', '.html')):
#def projectTreeRegister(fileTypes = ('.md')):
    """Aquire list of all markdown files and a rootBranch list."""
    #print('projectRoot[\'directories\']:')
    #print(directoryComprehension()['dirProjectDesignBuilder_Absolute'])

    """Aquire list of all markdown files in preperation for adding to the documentation."""
    #projectDocumentFiles = dict.fromkeys(fileTypes , [''])
    #projectDocumentFiles = {'html':[], 'rst':[], 'py':[], 'md':[]}
    #projectDocumentFiles = {}
        #projectDocumentFiles[fileType] = (['test'])




    projectFiles = []
    for subdir, dirs, files in walk(projectDirectory):
        for filez in files:
            for fileType in fileTypes:
                if(str(filez).endswith(fileType)):
                    projectFiles.append(str(path.join(subdir, filez)))

    projectDirectories = []
    for projectDirectory, pdirs, pfiles in walk(projectDirectory):
        for subdir in pdirs:
            #if str(subdir).find(".git") == -1:
            #if(('.git') not in str(subdir)):
                #print(subdir)
            pathDiscovery = str(path.join(projectDirectory, subdir))
            if(('.git') not in str(pathDiscovery)):
                #print(pathDiscovery)
                projectDirectories.append(pathDiscovery)


                    #print(path.join(subdir, filez))
                    #projectFiles = str(path.join(subdir, filez))
                    #projectDocumentFiles[fileType].extend([fileAppend])
                    #projectDocumentFiles[fileType].extend([str(path.join(subdir, filez))])
                    #projectDocumentFiles[fileType, []].append(path.join(subdir, filez))
                #projectDocumentFiles.append(path.join(subdir, filez))
                #print(path.join(subdir, file))
            #projectDocumentFiles[fileType]+=([fileAppend])
    """Aquire branches to all project directories.
    This will be implemented later."""
    #for fileType in fileTypes:
        ##projectDocumentFiles[fileType] = (['test'])
        #for subdir, dirs, files in walk(getcwd()):
            #for filez in files:
                #if(str(filez).endswith(fileType)):
                    ##print(path.join(subdir, filez))
                    ##projectFiles = str(path.join(subdir, filez))
                    #projectDirectories.append(str(path.join(subdir, filez)))

    #for subdir, dirs, files in walk(getcwd()):
        #for directory in dirs:
            #if(str(filez).endswith(fileType)):
                #projectDocumentFiles.append(path.join(subdir, filez))
                ##print(path.join(subdir, file))

    #"""Aquire branches to root project path. Add these to `sysPath`."""
    #rootBranch = []
    #for directory in listdir(getcwd()):
        #if(path.isdir(path.join(getcwd(), directory))):
            ##subDir = path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory)
            #if(str(directory).startswith('.') == False):
                #rootBranch.append(path.join(getcwd(), directory))
                ##print(path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory))


                #print(path.join(projectDirectory, subdir))


    del(projectDirectory)
    del(fileTypes)
    del(fileType)
    del(subdir)
    del(dirs)
    del(pdirs)
    del(filez)
    del(files)
    del(pfiles)
    del(pathDiscovery)
    return locals()



def main(operation = []):
    """Main discovery manager."""

    indent = ['', '  ', '    ', '        ']
    project = 'ProjectDesignBuilder'
    #confPath = ''/Manager/ # Path to conf.py file
    #pathDocTree = ''/Agents/ # Path to .doctree files
    #pathLog = ''/Logs/publish.log
    #pathSource = ''/Manager
    #pathOutput = ''/Proscribo
    #fileLog = publish.log

    print('[[ {} ]]\n'.format(path.basename(__file__)))

    # Querry the system to get absolute path for the project them make it current.
    projectDirectory(projectRoot = project )
    print('{}>>> [ projectDirectory(projectRoot = project) ]:\n'.format(indent[0]))
    for directory, directoryPath in projectDirectory(projectRoot = project).items():
        print('{}{}:\n{}{}'.format(indent[1], directory, indent[2], directoryPath))
        projectRoot = directoryPath
        #print(projectRoot)
    print()

    # Generate a project registry
    #print('{}>>> [ projectRegister() ]:\n'.format(indent[0]))
    #for directory, directoryPath in projectRegister().items():
        #print('{}{}:\n{}{}'.format(indent[1], directory, indent[2], directoryPath))
    #print()

    # Generate a project registry
    print('{}>>> [ projectTreeRegister() ]:\n'.format(indent[0]))
    for registry, field in projectTreeRegister(projectRoot).items():
        print('{}{}:'.format(indent[1], registry,))
        for entery in field:
            print('{}{}'.format(indent[2], entery))
        print()
    print()


    #files = ['test1.txt', 'test2.txt', 'test3.txt']
    #for i in range(len(files)):
        #print(files[i])

    ## Generate a project registry
    #print('{}>>> [ discovery() ]:\n'.format(indent[0]))
    #for directory, directoryPath in discovery().items():
        #print('{}{}:\n{}{}'.format(indent[1], directory, indent[2], directoryPath))
    #print()



    #local_register = report('registryTree', printReport = True)



    #sysPathAppend()
    #print(report(subject = 'directoryComprehension', returns = False))
    #report(subject = 'directoryComprehension', returns = False)

    #local_DirectoryComprehension = report('directoryComprehension', printReport = True)


    # 'sysPath' has all project directories appended is not starting with '.'.
    #local_sysPath = report('sysPath', printReport = False)

    #print(registerLocal)
    #print(report('registryTree', False))
    #report('sysPath')
    #discovery('directoryComprehension')




#'registry': ['/home/technicus/Projects/CAD/ProjectDesignBuilder/Administration', '/home/technicus/Projects/CAD/ProjectDesignBuilder/Builder', '/home/technicus/Projects/CAD/ProjectDesignBuilder/Design', '/home/technicus/Projects/CAD/ProjectDesignBuilder/Project'], 'register': '/home/technicus/Projects/CAD/ProjectDesignBuilder/Project'}





if __name__ == "__main__":
    main()







#  Scraps




#def getfunc():
    #"""getfunc is for conducting function call analysis."""
    #from inspect import currentframe, getframeinfo
    #caller = currentframe().f_back
    #func_name = getframeinfo(caller)[2]
    #caller = caller.f_back
    #from pprint import pprint
    #func = caller.f_locals.get(func_name, caller.f_globals.get(func_name))
    #return func



#def spawn_python_script(package_name, script_name, *args):
#def spawn_python_script(package_name, *args):
    #"""
    #Run the module ``script_name`` as an external Python script,
    #using the same Python executable as the current process,
    #with the same Python paths. This needs to support both
    #virtualenv and buildout Python executables.
    #Example:
        #popen = run_as_script('zetl.scripts','start_conductor.py')
    #Returns a :class:`subprocess.Popen` instance.
    #The `args` will be added as command line arguments.
    #"""

    ##script_path = resource_filename(package_name, script_name)

    #if args:
        ##params = [sys.executable, script_path] + list(args)
        #params = [executable, package_name] + list(args)
    #else:
        ##params = [sys.executable, script_path]
        #params = [executable, package_name]

    ## Build the PYTHONPATH environment variable needed by the child process
    ## in order to acquire the same sys.path values of the parent process.
    #python_path = ":".join(sysPath)[1:] # strip leading colon
    ##logging.info( "Running %s", params)
    #return subprocess.Popen(params, env={'PYTHONPATH':python_path}, shell=False, start_new_session = True) #, CREATE_NEW_CONSOLE = True)



#def discovery(operation = [], project = ''): # , printReport = False
    #"""Discovery function will reveal path and file information."""
    ##print('[[ DirectoryDiscovery.py :: discovery() ]]\n')

    #if('directoryComprehension' in operation):
        ##print('< directoryComprehension >\n')
        ##print('{}\n'.format(type(directoryComprehension())))
        #for directory, path in directoryComprehension().items():
            #print('{}:\n  {}\n'.format(directory, path))

    #if('directorySurvey' in operation):
        ##print('< directorySurvey >\n')
        ##directoryReview = directoryComprehension()['dirProjectDesignBuilder_Absolute']
        ##print('{}\n{}\n'.format(type(directoryReview), directoryReview))
        #survey = directorySurvey(directoryComprehension(project)['dirProjectDesignBuilder_Absolute'])
        ##for key, value in survey.items():
        #for key, value in directorySurvey(directoryComprehension(project)['dirProjectDesignBuilder_Absolute']).items():
            #print('{} :: {}'.format(key, value))
        #print('')
        ##print('dirProjectDesignBuilder_Absolute:\n{}\n'.format(directoryComprehension()['dirProjectDesignBuilder_Absolute']))
    ##print('{}\n'.format(locals()))
    #return 0

#def projectTreeRegister(projectRoot = directorySurvey(directoryComprehension()['dirProjectDesignBuilder_Absolute']), fileType = 'md'):
    #"""Aquire list of all markdown files and a rootBranch list."""
    ##print('projectRoot[\'directories\']:')
    ##print(directoryComprehension()['dirProjectDesignBuilder_Absolute'])

    #"""Aquire list of all markdown files in preperation for adding to the documentation."""
    #projectDocumentFiles = []
    #for subdir, dirs, files in walk(directoryComprehension()['dirProjectDesignBuilder_Absolute']):
        #for filez in files:
            #if(str(filez).endswith(fileType)):
                #projectDocumentFiles.append(path.join(subdir, filez))
                ##print(path.join(subdir, file))

    #"""Aquire branches to all project directories.
    #This will be implemented later."""
    ##projectDdirectoriess = []
    ##for subdir, dirs, files in walk(directoryComprehension()['dirProjectDesignBuilder_Absolute']):
        ##for filez in files:
            ##if(str(filez).endswith(fileType)):
                ##projectDocumentFiles.append(path.join(subdir, filez))
                ###print(path.join(subdir, file))

    #"""Aquire branches to root project path. Add these to `sysPath`."""
    #rootBranch = []
    #for directory in listdir(directoryComprehension()['dirProjectDesignBuilder_Absolute']):
        #if(path.isdir(path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory))):
            ##subDir = path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory)
            #if(str(directory).startswith('.') == False):
                #rootBranch.append(path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory))
                ##print(path.join(directoryComprehension()['dirProjectDesignBuilder_Absolute'], directory))

    #del(projectRoot)
    #del(fileType)
    #del(subdir)
    #del(dirs)
    #del(filez)
    #del(files)
    #del(directory)
    #return locals()



    #dirCurrent = getcwd()
    #print(projectRoot)
    # Get current directory
    #print(dirCurrent)
    #head_tail = path.split(dirCurrent)
    #print(head_tail)
    #dirWorking = head_tail[0]
    #print(head_tail[0])
    #pathBaseCurrent = '/' + path.basename(dirCurrent)
    #print(head_tail[1])
    # Absolute path for project.
    #print(dirProject_Absolute)
    # Get current directory
    #print(dirCurrent)
    #substring = str(dirCurrent).split(project)
    #dirProjectDesignBuilder_Absolute = dirCurrent[:dirCurrent.index(project) + len(project)]
    #print(dirProjectDesignBuilder_Absolute)
    #dirProjectDesignBuilder_Relative = relpath(dirProjectDesignBuilder_Absolute, dirCurrent) + '/' # Relative path to current directory from project
    #chdir(dirCurrent[:dirCurrent.index(project) + len(project)])
    #print(dirProjectDesignBuilder_Relative)
    #chdir('/home/technicus/Projects/CAD/ProjectDesignBuilder')
    #dirCurrent = getcwd()
    #head_tail = path.split(dirCurrent)
    #dirWorking = head_tail[0]
    #pathBaseCurrent = '/' + path.basename(dirCurrent)


    #dirDocTre_Relative = relpath(dirCurrent, dirDocTree) + '/' + dirDocTree # Relative path to current directory from project
    #dirConf_Relative = relpath(dirCurrent, dirConf) + '/' + dirConf# Relative path to current directory from project
    #dirLog_Relative = relpath(dirCurrent, dirLog) + '/' + dirLog# Relative path to current directory from project
    #dirSource_Relative = relpath(dirCurrent, dirSource) + '/' + dirSource# Relative path to current directory from project
    #dirOutput_Relative = relpath(dirProjectDesignBuilder_Absolute, dirOutput) + '/'# Relative path to current directory from project
    #dirOutput_Relative = relpath(dirOutput, dirProjectDesignBuilder_Absolute) + '/'# Relative path to current directory from project

    # Relational pathways.
    #dirProjectDesignBuilder_Relative = relpath(dirProjectDesignBuilder_Absolute, dirCurrent) + '/' # Relative path to current directory from project
    #dirDocTre_Relative = relpath(dirProjectDesignBuilder_Absolute, dirDocTree) + '/' # Relative path to current directory from project
    #dirConf_Relative = relpath(dirProjectDesignBuilder_Absolute, dirConf) + '/' # Relative path to current directory from project
    #dirLog_Relative = relpath(dirProjectDesignBuilder_Absolute, dirLog) + '/' # Relative path to current directory from project
    #dirSource_Relative = relpath(dirProjectDesignBuilder_Absolute, dirSource) + '/' # Relative path to current directory from project
    #dirOutput_Relative = relpath(dirProjectDesignBuilder_Absolute, dirOutput) + '/' # Relative path to current directory from project

    #dirProject = project
    #dirDocTree = 'Agents' # Path to .doctree files
    #dirConf = 'Manager' # Path to conf.py file
    #dirLog = 'Logs'
    #dirSource = 'Manager'
    #dirOutput = 'Proscribo'

    #dirCurrent_Relative = relpath(getcwd(), getcwd()) + '/'

    #del(projectRoot)
    #del(head_tail)
    #return locals()

