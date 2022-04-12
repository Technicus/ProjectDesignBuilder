#!/bin/python
# ProjectAssistant.py

import subprocess
from sys import exit, argv, exit
#from getopt import GetoptError, getopt, usage
from argparse import ArgumentParser, HelpFormatter, _SubParsersAction

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
    subprocess.run(
        args = [
        './Administration/Documentum/Publisher/Author/Publisher.py'
        ], shell=True
    )
    print()


def run_git():
    commit_message = input("\nCommit message: ")
    if commit_message is None:
        commit_message = []
    else:
        commit_message = commit_message
    subprocess_test = subprocess.run(
        args = [
        'git status; git add .; git status; git commit -m \"' + \
        commit_message + '\"; git status; git push; git status'
        ], shell=True
    )
    print()


    #parser = ArgumentParser(description='Project Assistant')
    #parser.add_argument(
        #'integers',
        #metavar='N',
        #type=int,
        #nargs='+',
        #help='an integer for the accumulator'
    #)
    #parser.add_argument(
        #'--sum',
        #dest='accumulate',
        #action='store_const',
        #const=sum,
        #default=max,
        #help='sum the integers (default: find the max)')

    #args = parser.parse_args()
    #print(args.accumulate(args.integers))



    #print(argv)
    #help_message = \
    #'ProjectAssistant.py [ -p | --push || -p | --publish || -h | --help ]\n'
    #print(argv)
    #print()
    #try:
        #opts, args = getopt(argv,"hup:", ["--help", "--push", "--publish" ])
    #except GetoptError as err:
        ## print help information and exit:
        #print(err)  # will print something like "option -a not recognized"
        #usage()
        #exit(2)
    #for opt, arg in opts:
        #if opt in ("-h", "--help"):
            #print(help_message)
            #exit()
            ##return 'problemo'
        #elif opt in ("-u", "--push"):
            #run_git(commit_message)
            #return 'git'
        #elif opt in ("-p", "--publish"):
            #run_publisher()
            #return 'publish'


def main(argv):
#def main():
    #subprocess.run('clear')
    print()
    #print(evaluate_arguments(argv))
    #print(evaluate_arguments())
    operation = evaluate_arguments(argv).constant_value
    #print(operation)
    if 'push' in operation:
        print(operation)
        run_git()

    if 'publish' in operation:
        print(operation)
        run_publisher()

    print()



if __name__ == "__main__":
    #main(argv[1:])
    main(argv)









