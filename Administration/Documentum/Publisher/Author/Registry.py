# Registry.py

from os import path, getcwd, chdir, walk
from os.path import relpath


def registry(projectRoot = getcwd(), projectName = '', directoryOmit = (), fileRegisterTypes = ()):
    """Return a list of files and a list of directories.
        This function will identify necessary path information.  Then
        also change current working directory to absolute path of
        project root."""
    chdir(projectRoot)
    projectDirectory = projectRoot
    workRoot = projectDirectory
    projectFiles = []
    for subdir, dirs, files in walk(projectDirectory):
        for filez in files:
            for fileType in fileRegisterTypes:
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
            if any(omission in pathDiscovery for omission in directoryOmit):
                pass
            else:
                pathRelation = path.relpath(subdir, projectDirectory)
                pathRelation = subdir.partition(projectDirectory)[1:]
                workDir = path.basename(projectDirectory)
                pathTail = path.basename(workRoot)
                pathHead = pathDiscovery.split(pathTail, 1)
                projectDirectories.append('.' + pathHead[1])
    registry = {'projectRoot':[workRoot], 'projectDirectories':projectDirectories, 'projectFiles':projectFiles,}
    return registry


def registryReport(registry = {}):
    for register, field in registry.items():
        print('  {}:'.format(register,))
        for entery in field:
            print('    {}'.format(entery))
        print()


def registryQuery(registry = {}, search = []):
    searchResult = []
    for register, field in registry.items():
        for entery in field:
            if any(searchField in entery for searchField in search):
                searchResult.append(str(entery))
    return searchResult

