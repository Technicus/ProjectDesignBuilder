#!/bin/python

from sys import path as sysPath, executable
from os import system, path, getcwd, chdir, scandir, listdir, walk
from os.path import relpath
import subprocess
#import logging


def registry(projectRoot = 'none', fileTypes = ('.md', '.py', '.rst', '.html')):
    """Return a list of files and a list of directories.
        This function will identify necessary path information.  Then
        also change current working directory to absolute path of
        project root."""
    head_tail = getcwd().split(projectRoot)
    projectRoot = head_tail[0] + projectRoot
    chdir(projectRoot)
    projectDirectory = projectRoot
    workRoot = projectDirectory
    projectFiles = []
    for subdir, dirs, files in walk(projectDirectory):
        for filez in files:
            for fileType in fileTypes:
                pathDiscovery = str(path.join(projectDirectory, subdir))
                if(str(filez).endswith(fileType)):
                    pathRelation = path.relpath(subdir, projectDirectory)
                    pathRelation = subdir.partition(projectDirectory)[1:]
                    workDir = path.basename(projectDirectory)
                    pathTail = path.basename(workRoot)
                    pathHead = pathDiscovery.split(pathTail, 1)
                    filezPath = '.' + pathHead[1]
                    projectFiles.append(str(path.join(filezPath, filez)))
    projectDirectories = []
    for projectDirectory, pdirs, pfiles in walk(projectDirectory):
        for subdir in pdirs:
            pathDiscovery = str(path.join(projectDirectory, subdir))
            if(('.git') not in str(pathDiscovery)):
                pathRelation = path.relpath(subdir, projectDirectory)
                pathRelation = subdir.partition(projectDirectory)[1:]
                workDir = path.basename(projectDirectory)
                pathTail = path.basename(workRoot)
                pathHead = pathDiscovery.split(pathTail, 1)
                projectDirectories.append('.' + pathHead[1])
    registry = {'projectRoot':[workRoot], 'projectDirectories':projectDirectories, 'projectFiles':projectFiles,}
    return registry


def main(operation = []):
    """Main discovery manager."""
    indent = ['', '  ', '    ', '        ']
    project = 'ProjectDesignBuilder'
    print('[[ {} ]]\n'.format(path.basename(__file__)))
    # Generate a project registry
    print('{}>>> [ registry() ]:\n'.format(indent[0]))
    for register, field in registry(projectRoot = project).items():
        print('{}{}:'.format(indent[1], register,))
        for entery in field:
            print('{}{}'.format(indent[2], entery))
        print()
    #chdir(projectRoot)
    #print(registry(projectRoot = project)['projectRoot'])

if __name__ == "__main__":
    main()
