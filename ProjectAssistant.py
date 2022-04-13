#!/bin/python
# ProjectAssistant.py


from subprocess import run
from sys import exit, argv, exit
#from getopt import GetoptError, getopt, usage
from argparse import ArgumentParser, HelpFormatter, _SubParsersAction
from os import chdir, path, getcwd
import readline

class CapitalisedHelpFormatter(HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = 'Usage: '
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)


class CustomHelpFormatter(HelpFormatter):
    #https://bugs.python.org/issue39106
    #https://microeducate.tech/customize-argparse-help-message/
    #https://riptutorial.com/python/example/25313/argparse--custom-help-formatter-
    def _format_action(self, action):
        if type(action) == _SubParsersAction:
            # inject new class variable for subcommand formatting
            subactions = action._get_subactions()
            invocations = [self._format_action_invocation(a) for a in subactions]
            self._subcommand_max_length = max(len(i) for i in invocations)

        if type(action) == _SubParsersAction._ChoicesPseudoAction:
            # format subcommand help line
            subcommand = self._format_action_invocation(action) # type: str
            width = self._subcommand_max_length
            help_text = ""
            if action.help:
                help_text = self._expand_help(action)
            return "  {:{width}} -  {}\n".format(subcommand, help_text, width=width)

        elif type(action) == _SubParsersAction:
            # process subcommand help section
            msg = '\n'
            for subaction in action._get_subactions():
                msg += self._format_action(subaction)
            return msg
        else:
            return super(CustomHelpFormatter, self)._format_action(action)


def evaluate_arguments(argv):
#def evaluate_arguments():
    # hack to show help when no arguments supplied

    #parser = ArgumentParser(add_help=False, formatter_class=CustomHelpFormatter)
    parser = ArgumentParser(add_help=True, formatter_class=CustomHelpFormatter)
    #parser = ArgumentParser(add_help=True)

    if len(argv) == 1:
        parser.print_help()
        print()
        exit(0)

    parser.add_argument('-u', '--push', action='store_const', dest='constant_value',
                    const='push',
                    help='Push to GitHub.')
    parser.add_argument('-p', '--publish', action='store_const', dest='constant_value',
                    const='publish',
                    help='Publish documentation.')
    return parser.parse_args()


def run_publisher():
    #chdir('./Administproject_rootration/Documentum/Publisher/Author')
    run(
        args = [
        #'./Publisher.py'
        './Administration/Documentum/Publisher/Author/Publisher.py'
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


def run_git(cache_file = None):
    subprocess = run(
        args = [
        'git status; \
        git add .; git status;'\
        ], shell=True
    )

    with open(cache_file, 'r') as cache:
        previous_commit_message = cache.readlines()[-1].rstrip()

    #commit_message = input("\nCommit message: ")
    commit_message = input_with_prefill('Commit message: ',
        previous_commit_message)
    #print(commit_message)
    if commit_message is None:
        commit_message = []
    else:
        commit_message = commit_message
    with open(cache_file, 'a') as cache:
        cache.write(f'\n{commit_message}')
    #print()
    subprocess = run(
        args = [
        'git commit -m \"' + commit_message + '\"; git status; \
        git push; git status'
        ], shell=True
    )
    print()

def set_current_working_directory():
    #print(f'`path.abspath(getcwd())`:\n[ {path.abspath(getcwd())} ]\n')
    #print(f'`path.dirname(path.abspath(__file__))`:\n[ {path.dirname(path.abspath(__file__))} ]\n')
    if path.abspath(getcwd()) is not path.dirname(path.abspath(__file__)):
        chdir(path.dirname(path.abspath(__file__)))
    #print(f'`path.abspath(getcwd())`:\n[ {path.abspath(getcwd())} ]\n')
    #print(f'`path.dirname(path.abspath(__file__))`:\n[ {path.dirname(path.abspath(__file__))} ]\n')


def main(argv):
    cache_file = './Builder/Utilities/Data/Cache/assistant.cache'
    run('clear')
    set_current_working_directory()
    assistant_cache_file = open(cache_file, 'a')
    assistant_cache_file.write('')
    assistant_cache_file.close()

    #print()
    #print(evaluate_arguments(argv))
    #print(evaluate_arguments())
    operation = evaluate_arguments(argv).constant_value
    if 'push' in operation:
        #print(operation)
        run_git(cache_file)

    if 'publish' in operation:
        #print(operation)
        run_publisher()
    #print()


if __name__ == "__main__":
    #main(argv[1:])
    main(argv)
