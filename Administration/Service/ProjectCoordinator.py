#!/bin/python


from subprocess import run, PIPE
from sys import exit, argv, stderr #, stdout
from argparse import ArgumentParser, HelpFormatter, _SubParsersAction, RawTextHelpFormatter, ArgumentError
from os import chdir, path, getcwd
import readline
from datetime import date, datetime

from contextlib import redirect_stdout, redirect_stderr

from io import StringIO



#class RedirectStdStreams(object):
    #def __init__(self, stdout=None, stderr=None):
        #self._stdout = stdout #or stdout
        #self._stderr = stderr #or stderr

    #def __enter__(self):
        #self.old_stdout, self.old_stderr = stdout, stderr
        #self.old_stdout.flush(); self.old_stderr.flush()
        #stdout, stderr = self._stdout, self._stderr

    #def __exit__(self, exc_type, exc_value, traceback):
        #self._stdout.flush(); self._stderr.flush()
        #stdout = self.old_stdout
        #stderr = self.old_stderr


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
            pass
            #print(f"***** argparse._HelpAction")

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
            #print(f"{help_str}")
            #help_str = str(help_list).strip('[\'').strip('\']') # + '\n '
            return help_str + ' \n '
            #return helper + ' \n'
            #return helper


def parse_arguments(cache_file = None, arguments = argv[1:]):
#def evaluate_arguments(arguments = argv):
#def evaluate_arguments():
#def evaluate_arguments():
    # hack to show help when no arguments supplied
    #parser = ArgumentParser(add_help=False, formatter_class=CustomHelpFormatter)
    parser = ArgumentParser(
        prog='program',
        usage='usage',
        description='description',
        epilog = 'epilog',
        add_help = False,
        exit_on_error = False,
        allow_abbrev = False,
        #formatter_class = CustomHelpFormatter,
        #formatter_class = RawTextHelpFormatter,
        )
    #if len(arguments) == 0:
        #parser.print_help()
        #print()
        #exit(0)

    parser.add_argument(
        '-u',
        '--push',
        action ='store_const',
        # dest ='push',
        const ='push',
        help ='Push to GitHub.'
    )
    parser.add_argument(
        '-p', '--publish',
        action ='store_const',
        # dest ='publish',
        const ='publish',
        help ='Publish documentation.'
    )
    parser.add_argument(
        '-h',
        '--help',
        action ='store_const',
        # dest ='parser_help',
        const ='parser_help',
        help ='Explain how this operates.'
    )
    parser.add_argument(
        '-t',
        '--test',
        action = 'store',
        required = False,
        nargs = '*',
        #default = [],
        help ='Test argument.'
    )

    with open(cache_file, 'w') as argparse_file:
        """This is rather messy but seems to do most of what it is intended
        to do.  Error handeling is not being managed very well."""
        with redirect_stdout(argparse_file):
            with redirect_stderr(argparse_file):
                #error_file = StringIO()
                #with RedirectStdStreams(stdout=argparse_file, stderr=argparse_file):
                print('[ Argparse Results ]\n')
                try:
                    unknown = None
                    arguments, unknown = parser.parse_known_args()
                except ArgumentError:
                    #redirect_stderr = redirect_stdout
                    #with redirect_stderr(error_file):
                        #print('Hello', file=stderr)
                    print(f"ArgumentError \n")
                    #print(f"{str(redirect_stderr)}")
                    #parser.print_help()
                    argument_error = True
                if hasattr(arguments, '__dict__'):
                    print(f"Arguments:")
                    print(f"  Known:")    # {dict(vars(arguments))}")
                    for argument, parameter in dict(vars(arguments)).items():
                        print(f"    {argument} : {parameter}")
                    if len(unknown) > 0:
                        print(f"  Unknown:")
                        for argument in unknown:
                            print(f"    {argument}")
                else:
                    #parser.print_help()
                    if arguments == None:
                        print(f"ArgumentError \n")
                        print(f"No arguments")
                #if dict(vars(arguments))['help']:
                print(f"\nHelp dialog:\n")
                parser.print_help()

    # evaluation of help
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

    return arguments, unknown


    #args, unknown = parser.parse_known_args()
    #print(f"  Register arguments:\n    {register.registry.get('arguments')('known')}\n")

    #print(register.arguments)
    #print(parser.amespace())
    #for arttribute in dir(parser):
        #print(arttribute)
    #if parser_help:
        #parser.print_help()
        #print()

    #print(*a, file = stdout)




def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result

