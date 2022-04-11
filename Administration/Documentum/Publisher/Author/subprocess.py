
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

