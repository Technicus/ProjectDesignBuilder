#!/bin/python

from os import path, getcwd, chdir, walk
from os.path import relpath


def registry(projectRoot = getcwd(), projectName = '', directoryOmit = (), fileRegisterTypes = ()):
    """Return a list of files and a list of directories.
        This function will identify necessary path information.  Then
        also change current working directory to absolute path of
        project root."""
    #head_tail = getcwd().split(projectRoot)
    #projectRoot = head_tail[0] + projectRoot
    #print('cwd = {}'.format(getcwd()))
    chdir(projectRoot)
    #print('projectRoot = {}'.format(projectRoot))
    projectDirectory = projectRoot
    #print('projectDirectory = {}'.format(projectDirectory))
    workRoot = projectDirectory
    #print('workRoot = {}'.format(workRoot))
    projectFiles = []
    for subdir, dirs, files in walk(projectDirectory):
        #print('subdir = {}'.format(subdir))
        #print('dirs = {}'.format(dirs))
        #print('files = {}'.format(files))
        for filez in files:
            for fileType in fileRegisterTypes:
                pathDiscovery = str(path.join(projectDirectory, subdir))
                if(str(filez).endswith(fileType)):
                    #print('subdir = {}'.format(subdir))
                    #print('pathDiscovery = {}'.format(pathDiscovery))
                    #print('filez = {}'.format(filez) )
                    pathRelation = path.relpath(subdir, projectDirectory)
                    #print('pathRelation_0 = {}'.format(pathRelation))
                    pathRelation = subdir.partition(projectDirectory)[1:]
                    #print('pathRelation_1= {}'.format(pathRelation))
                    workDir = path.basename(projectDirectory)
                    #print('workDir = {}'.format(workDir))
                    pathTail = path.basename(workRoot)
                    #print('pathTail = {}'.format(pathTail))
                    pathHead = pathDiscovery.split(pathTail, 1)
                    #print('pathHead = {}'.format(pathHead))
                    filezPath = '.' + pathHead[1]
                    #print('filezPath = {}'.format(filezPath))
                    projectFiles.append(str(path.join(filezPath, filez)))
                    #print('projectFiles = {}'.format(projectFiles))
    projectDirectories = []
    for projectDirectory, pdirs, pfiles in walk(projectDirectory):
        for subdir in pdirs:
            pathDiscovery = str(path.join(projectDirectory, subdir))
            #if((directoryOmit) not in str(pathDiscovery)):
            if(str(pathDiscovery) not in directoryOmit):
                #for omission in directoryOmit :
                    #if(str(omission) not in str(pathDiscovery)):
                pathRelation = path.relpath(subdir, projectDirectory)
                pathRelation = subdir.partition(projectDirectory)[1:]
                workDir = path.basename(projectDirectory)
                pathTail = path.basename(workRoot)
                pathHead = pathDiscovery.split(pathTail, 1)
                projectDirectories.append('.' + pathHead[1])

    dirCount = 0
    for directory in projectDirectories:
        for omission in directoryOmit :
            if str(directory).find(str(omission)) != -1:
                print("[ {} ]> del projectDirectories[ {} ]".format(dirCount, directory))
                del projectDirectories[dirCount]
        dirCount += 1

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
