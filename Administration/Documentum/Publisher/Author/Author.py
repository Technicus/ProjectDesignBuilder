# Author.py


from sys import path as sysPath, argv
from os import walk, path, getcwd, system


'''
.. toctree::
   :caption: Title
   :maxdepth: 1

   path/restructuredText
'''


headdersMainTOC = ['Admin Guide', 'API', 'Installation', 'Development', 'Contribute', 'Reference', 'About', 'Project', 'Design', 'Build']
headdersDirectory

for agent in files:
        #print(path.join(dirRoot, name))
        agentFile = path.join(agentLead, agent)
        agent_split = path.split(agentFile)
        agentPath = agent_split[0]
        agentPath_split = path.split(agentPath)
        agentLeader = agentPath_split[1]
        agentQuery_List = open("agentQuery.list", "a")
        agentQuery_List.write('{}\n'.format(agentLeader))
        agentQuery_List.write('{}\n\n'.format(agent))
        agentQuery_List.close()
        #agentQuery_List.write('agentLeader\n{}\n'.format(agentLeader))
        #agentQuery_List.write('agentFile\n{}\n'.format(agentFile))
        #agentQuery_List.write('agentPath\n{}\n\.'.format(agentPath))

def agentQuery():
    for agent in dirs:
            #if(name != '__pycache__'):
            dirWorkingAbs = path.join(agentLead, agent)
            sysPath.append(dirWorkingAbs)

            agentFile = dirWorkingAbs

            agent_split = path.split(agentFile)
            agentPath = agent_split[0]

            agentPath_split = path.split(agentPath)
            agentLeader = agentPath_split[1]

            #print('agent :: {}\n-------------'.format(agent))
            #print('[ agentPath ]\n(\'{}\')'.format(agentPath))
            #print('[ agentLead ]\n(\'{}\')\n'.format(agentLead))
            agentQuery_List = open("agentQuery.list", "a")
            #agentQuery_List.write('[ {} ]\n'.format(agent))
            agentQuery_List.write('{}\n'.format(agentLeader))
            agentQuery_List.write('{}\n\n'.format(agent))
            #agentQuery_List.write('( agentFile )\n{}\n'.format(agentFile))
            #agentQuery_List.write('( agentPath )\n{}\n'.format(agentPath))
            #agentQuery_List.write('( agentLeader )\n{}\n\n'.format(agentLeader))
            agentQuery_List.close()
            agentQuery_List = open("agentQuery.list", "r")
            #print('\n{}'.format(agentQuery_List.read()))
            agentQuery_List.close()
            print('agentQuery.list\n')


#def spawn_python_script(package_name, script_name, *args):
def spawn_python_script(package_name, *args):
    """
    Run the module ``script_name`` as an external Python script,
    using the same Python executable as the current process,
    with the same Python paths. This needs to support both
    virtualenv and buildout Python executables.
    Example:
        popen = run_as_script('zetl.scripts','start_conductor.py')
    Returns a :class:`subprocess.Popen` instance.
    The `args` will be added as command line arguments.
    """
    #script_path = resource_filename(package_name, script_name)
    if args:
        #params = [sys.executable, script_path] + list(args)
        params = [executable, package_name] + list(args)
    else:
        #params = [sys.executable, script_path]
        params = [executable, package_name]

    # Build the PYTHONPATH environment variable needed by the child process
    # in order to acquire the same sys.path values of the parent process.
    python_path = ":".join(sysPath)[1:] # strip leading colon
    #logging.info( "Running %s", params)
    return subprocess.Popen(params, env={'PYTHONPATH':python_path}, shell=False, start_new_session = True) #, CREATE_NEW_CONSOLE = True)


