#!/bin/python


from subprocess import run, PIPE
from sys import exit, argv, exit
from argparse import ArgumentParser, HelpFormatter, _SubParsersAction, RawTextHelpFormatter
from os import chdir, path, getcwd
import readline
from datetime import date, datetime


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
        help_list = []
        if type(action) == 'argparse._HelpAction':
            print(f"***** argparse._HelpAction")

        if type(action) == _SubParsersAction:
            # inject new class variable for subcommand formatting
            subactions = action._get_subactions()
            invocations = [self._format_action_invocation(a) for a in subactions]
            self._subcommand_max_length = max(len(i) for i in invocations)
            self._subcommand_max_length = self._subcommand_max_length + '\n'

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
            return msg + '\n'

        else:
            helper = (f"{super(CustomHelpFormatter, self)._format_action(action)}")
            #print(f"***test***")
            #print(f"*  action: \n     {action}")
            #print(f"*  type: \n     {type(action)}\n")
            #print(action)
            #type(action)
            help_list.append(str(helper).strip('\n'))
            #help_list[0] = ' ' + help_list[0]
            help_str = str(help_list).strip('[\'').strip('\']') # + '\n '
            help_str.replace('-', '•')
            print(f"{help_str}")
            #help_str = str(help_list).strip('[\'').strip('\']') # + '\n '
            return help_str + ' \n '
            #return helper + ' \n'
            #return helper


def evaluate_arguments(arguments = argv[1:]):
#def evaluate_arguments(arguments = argv):
#def evaluate_arguments():
#def evaluate_arguments():
    # hack to show help when no arguments supplied
    #parser = ArgumentParser(add_help=False, formatter_class=CustomHelpFormatter)
    parser = ArgumentParser(
        add_help = True,
    """ this is fukn gay and it is pissin me off
    I am trying to get the help to print an extra line after the end of output
    before being returned to the prompt.
    The answer is around here somewhere:
    https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter
    If `formatter_class = CustomHelpFormatter` is set and a space is added to
    ` \n`a new line will be added but the indentation will be offset.
    If `\n` is added there will be lines between opetions.
    This is a waste of my life.
    """
        formatter_class = CustomHelpFormatter,
        #formatter_class = RawTextHelpFormatter)
    #parser = ArgumentParser(add_help = True, formatter_class = RawTextHelpFormatter)
    #parser = ArgumentParser(add_help=True)
    #parser = ArgumentParser(description='test', formatter_class=RawTextHelpFormatter)

    if len(arguments) == 0:
        parser.print_help()
        #print()
        #exit(0)

    parser.add_argument('-u', '--push', action='store_const', dest='constant_value',
                    const='push',
                    help='Push to GitHub.')
    parser.add_argument('-p', '--publish', action='store_const', dest='constant_value',
                    const='publish',
                    help='Publish documentation.')

    return parser.parse_args()



def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result

