
from subprocess import run, PIPE
from sys import exit
#from argparse import ArgumentParser, HelpFormatter, _SubParsersAction
#from os import chdir, path, getcwd
import readline
#from datetime import date, datetime



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


def run_git(cache_file = None):
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
    print()
def run_git():
    subprocess_test = run(
        args = [
        'git status; \
        git add .; git status;'\
        ], shell=True
    )

    commit_message = input("\nCommit message: ")
    if commit_message is None:
        commit_message = []
    else:
        commit_message = commit_message
    print()

    subprocess_test = run(
        args = [
        'git commit -m \"' + commit_message + '\"; git status; \
        git push; git status'
        ], shell=True
    )
    print()


def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


def evaluate_arguments(arguments = None, register = None):
    pass
    #if dict(vars(arguments))['help']:
        #with open(cache_file, 'r') as argparse_file:
            #for line_count, line in enumerate(argparse_file, 1):
                #if 'Help dialog:' in line:
                #help_dialog_line = line_count
        #argparse_file.seek(1)
        #help_dialog = argparse_file.readlines()[help_dialog_line:line_count]
    #for line in help_dialog:
        #print(f"      {line.strip()}")
    #print(f"")
#def main(argv):
    cache_file = './Utilities/Data/Cache/assistant.cache'
    #run('clear')
    #set_current_working_directory()
    assistant_cache_file = open(cache_file, 'a')
    #assistant_cache_file.write('')
    assistant_cache_file.close()

    #print()
    #print(evaluate_arguments(argv))
    #print(evaluate_arguments())
    #operation = evaluate_arguments(argv).constant_value
    operation = []
    if 'push' in operation:
        #print(operation)
        run_git(cache_file)

    if 'publish' in operation:
        #print(operation)
        run_publisher()
    #print()

    #registry = Registry('./', 'ProjectDesignBuilder', ['.git', '__'],
        #['.md', '.py', '.rst', '.html'])
    #registry.report()
#def main(argv):
    #run('clear')
    #print()
    #print(evaluate_arguments(argv))
    #print(evaluate_arguments())
    #operation = evaluate_arguments(argv).constant_value
    operation = []

    if 'push' in operation:
        #print(operation)
        run_git()

    if 'publish' in operation:
        #print(operation)
        run_publisher()
    print()

