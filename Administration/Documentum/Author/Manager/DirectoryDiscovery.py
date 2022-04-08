#!/bin/python

from sys import path as sysPath
from os import walk, path, getcwd, system, scandir
from os.path import relpath

project = 'ProjectDesignBuilder'


def getfunc():
	"""getfunc is for conducting function call analysis."""
    from inspect import currentframe, getframeinfo
    caller = currentframe().f_back
    func_name = getframeinfo(caller)[2]
    caller = caller.f_back
    from pprint import pprint
    func = caller.f_locals.get(
            func_name, caller.f_globals.get(
                func_name
        )
    )

    return func


def directoryComprehension():
	"""directorySurvey will identify necessary path information."""
    #print('[[ DirectoryDiscovery.py :: directoryComprehension() ]]\n')
    dirCurrent = getcwd()
    dirCurrent_Relative = relpath(getcwd(), getcwd()) + '/'
    head_tail = path.split(dirCurrent)
    dirWorking = head_tail[0]
    del(head_tail)
    pathBaseCurrent = '/' + path.basename(dirCurrent)
    dirProjectDesignBuilder_Absolute = dirCurrent[:dirCurrent.index(project) + len(project)]
    dirProjectDesignBuilder_Relative = relpath(dirProjectDesignBuilder_Absolute, dirCurrent) + '/'
    #print("\ndirCurrent:\n========= \n{}".format(dirCurrent))
    #print("\ndirWorkingCurrent:\n=========\n{}".format(dirWorkingCurrent))
    #print("\npathBaseCurrent:\n=========\n{}".format(pathBaseCurrent))
    #dirProjectDesignBuilder_Absolute = path.abspath(dirProjectDesignBuilder_Relative)
    #print("\ndirProjectDesignBuilder_Absolute:\n========= \n{}".format(dirProjectDesignBuilder_Absolute))
    #print("\ndirProjectDesignBuilder_Relative:\n========= \n{}".format(dirProjectDesignBuilder_Relative))
    #print("\nsysPath:\n=========")# {}\n".format(sysPath))
    #for directory in sysPath:
        #print('{}'.format(directory))
    #print('')
    return locals()


def directorySurvey(directory):
	"""directorySurvey will conduct the work of finding information within a directory."""
    #print('[[ DirectoryDiscovery.py :: directorySurvey() ]]\n')
    directories = []
    files = []
    #print('Survey path:\n{}\n'.format(directory))
    with scandir(directory) as pathReview:
        #print('Directories:')
        for audit in pathReview:
            #if not audit.name.startswith('.') and audit.is_file():
            if not audit.name.startswith('.') and audit.is_dir():
                #print('  {}'.format(audit.name))
                directories.append(audit.name)
        #print('Files:')
    with scandir(directory) as pathReview:
        for audit in pathReview:
            if not audit.name.startswith('.') and audit.is_file():
                #print('  {}'.format(audit.name))
                files.append(audit.name)
    del(audit)
    del(pathReview)
    del(directory)
    #print('\nLocals():')
    #for key, value in locals().items():
        #print('{} : {}'.format(key, value))
    #print('')
    #print('{}\n'.format(locals()))
    return locals()

def discovery(operation = []): # , printReport = False
	"""Discovery function will reveal path and file information."""
    #print('[[ DirectoryDiscovery.py :: discovery() ]]\n')
    if('directoryComprehension' in operation):
        #print('< directoryComprehension >\n')
        #print('{}\n'.format(type(directoryComprehension())))
        for directory, path in directoryComprehension().items():
            print('{}:\n{}\n'.format(directory, path))

    if('directorySurvey' in operation):
        #print('< directorySurvey >\n')
        #directoryReview = directoryComprehension()['dirProjectDesignBuilder_Absolute']
        #print('{}\n{}\n'.format(type(directoryReview), directoryReview))
        survey = directorySurvey(directoryComprehension()['dirProjectDesignBuilder_Absolute'])
        #for key, value in survey.items():
        for key, value in directorySurvey(directoryComprehension()['dirProjectDesignBuilder_Absolute']).items():
            print('{} :: {}'.format(key, value))
        print('')
        #print('dirProjectDesignBuilder_Absolute:\n{}\n'.format(directoryComprehension()['dirProjectDesignBuilder_Absolute']))
    #print('{}\n'.format(locals()))
    return 0

def main(operation = []):
    """Main discovery manager."""
    print('[[ {} :: {} ]]\n'.format(path.basename(__file__), getfunc()))
    discovery(['directoryComprehension'])
    discovery('directorySurvey')


if __name__ == "__main__":
    main()
