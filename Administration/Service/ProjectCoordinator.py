
from subprocess import run, PIPE
from sys import exit
#from argparse import ArgumentParser, HelpFormatter, _SubParsersAction
#from os import chdir, path, getcwd
import readline
#from datetime import date, datetime
from ArgumentInterpreter import report_arguments
from Administrator import time_code



def run_publisher():
    #chdir('./Administration/project_rootration/Documentum/Publisher/Author')
    run(
        args = [
        #'./Publisher.py'
        "./Administration/Athenaeum/Publisher/Director/PublishingDirector.py"
        #'./Administration/Documentum/Publisher/Author/Publisher.py'
        ], shell=True
    )
    #print()
    #run(
        #args = [
        ##'./Publisher.py'
        #'ls'
        #], capture_output = True, shell = False
    ##)
    #run(['ls', '-l'], stdout=PIPE).stdout.decode('utf-8')
        #getoutput("ls -l")
    #print(run(['ls', '-l'], stdout=PIPE).stdout.decode('utf-8'))
    #run(['ls -l'], shell = True)
    #cmd = ['awk', 'length($0) > 5']
    #ip = 'foo\nfoofoo\n'.encode('utf-8')
    #result = run(cmd, stdout=PIPE, input=ip).stdout.decode('utf-8')
    ##result.stdout.decode('utf-8')
    #print(result)
#def run_publisher():
    #run(
        #args = [
        #'./Administration/Documentum/Publisher/Author/Publisher.py'
        #], shell=True
    #)
    #print()


def push(cache_file = None):
    with open(cache_file, 'r') as cache:
        previous_commit_message = cache.readlines()[-1].rstrip()
    subprocess = run(
        args = [
        'git status; \
        git add .; git status;'\
        ], shell=True
    )
    #commit_message = input("\nCommit message: ")
    commit_message = input_with_prefill('Commit message: ',
        previous_commit_message)
    #print(commit_message)
    if commit_message is None:
        commit_message = []
    else:
        commit_message = commit_message
    subprocess = run(
        args = [
        'git commit -m \"' + commit_message + '\"; \
        git push; git status'
        ], shell=True
    )
    with open(cache_file, 'a') as cache:
        cache.write(f'\n{time_code()}\n{commit_message}')
    #print()
    #print()

#def run_git():
    #subprocess_test = run(
        #args = [
        #'git status; \
        #git add .; git status;'\
        #], shell=True
    #)

    #commit_message = input("\nCommit message: ")
    #if commit_message is None:
        #commit_message = []
    #else:
        #commit_message = commit_message
    ##print()

    #subprocess_test = run(
        #args = [
        #'git commit -m \"' + commit_message + '\"; git status; \
        #git push; git status'
        #], shell=True
    #)
    ##print()


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


def evaluate_arguments(register = None):

    from Typographer import clear
    clear()

    #test_file = register.search('test.cache')
    cache_file = register.search('assistant.cache')

    # Default help flag changes to false if any other argument is not None,
    # unless register 'help' argument is True.
    argument_help = True
    # Check git upload flag.
    if dict(vars(register.arguments['known'])).get('push'):
        argument_help = False
        print(f"[ Push ]\n")
        #print(f"\n  push: ", end = (""))
        #print(f"{dict(vars(register.arguments['known'])).get('push')}\n")
        push(''.join(cache_file))
    # Check publish upload flag.
    if dict(vars(register.arguments['known'])).get('publish'):
        argument_help = False
        print(f"\n  publish: ", end = (""))
        print(f"{dict(vars(register.arguments['known'])).get('publish')}\n")        #run_git(cache_file)
    # Check meta upload flag.
    if dict(vars(register.arguments['known'])).get('meta'):
        argument_help = False
        print(f"\n  meta: ", end = (""))
        print(f"{dict(vars(register.arguments['known'])).get('meta')}\n")        #run_git(cache_file)
    # Checking for help.
    #if dict(vars(register.arguments['known'])).get('help'):
        #pass
        #print(f"  help: ", end = (""))
        #print(f"{dict(vars(register.arguments['known'])).get('help')}\n")        #run_git(cache_file)
    # Help starts as true.
    if argument_help | dict(vars(register.arguments['known'])).get('help'):
        #print(f"[ evaluate_arguments ]")
        #print(f"\n  cache_file:\n    {cache_file}")
        #print(f"  test_file:\n    {test_file}")
        #print()
        report_arguments(register)
        print(f"  argument_help: {argument_help}\n")
