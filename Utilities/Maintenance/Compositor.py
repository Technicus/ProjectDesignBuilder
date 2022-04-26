# Typographer.py
# 2022.04.20.21.57

from os import get_terminal_size
from inspect import currentframe, stack
from os import system
from importlib import import_module as invoke
from colorama import Fore, Back, Style
from termcolor import colored, cprint

#from inspect import currentframe  # , getframeinfo, trace


project_name = invoke('ProjectDesignBuilder', '').project_name
__version__ = invoke('ProjectDesignBuilder', '').__version__
__release__ = invoke('ProjectDesignBuilder', '').__release__
indent = ['', '  ', '    ', '        ']


def clear():
    """This function only has support to clear the screen for Linux of Mac."""
    _ = system("clear")


def headding_section(marker = None, title = None):
    """This funciton returns a section for printing to console or adding
    to logs to seperate process for improving readability.  It also
    provides some process information.  This can be improved with more
    development of process_inspection()."""
    if marker is None:
        marker = '='
        #headding_prefix = '\n='
        headding_prefix = '='
        line_difference = 2
    else:
        #headding_prefix = '\n--'
        headding_prefix = '--'
        line_difference = 3
    terminal_size = get_terminal_size()
    if title == None:
        working_file = __file__.split('/')
        title = f"[ {working_file} ] : {str(currentframe().f_back.f_lineno)} ]"
                #len(working_file[-1]) - 11 )
    marker = marker * (terminal_size.columns - len(title) - line_difference)
    section = f"{headding_prefix}{title} {marker}"
    return section


def check_string(string, substring_list):
    for substring in substring_list:
        if substring in string:
            return True
    return False


def check_list(super_string_list = None, sub_string_list = None):
    if any(sub_string_list in super_string_list):
        pass

    else:
        pass


# Expects a list and will convert it to a string and return the string
def listToString(inList):
    functionStatus()
    outString = ""
    if len(inList) == 1:
        outString = outString + str(inList[0])
    if len(inList) > 1:
        outString = outString + str(inList[0])
        for items in inList[1:]:
            outString = outString + str(items)
    return outString


def formatConfig(inString):
    functionStatus()
    #inString = inString.lstrip('"')
    #inString = inString.rstrip('"')
    disallowed_characters = "\""
    #for character in disallowed_characters:
        #inString = inString.replace(character, "")
    inString = inString.replace(disallowed_characters   , "")
    return inString


def pathto_dict(path_):
    for root, dirs, files in walk(path_):
        tree = {'name': root, 'type':'folder', 'children':[]}
        tree['children'].extend([pathto_dict(path.join(root, d)) for d in dirs])
        tree['children'].extend([{'name':path.join(root, f), 'type':'file'} for f in files])
        return tree


def section(headder="section", title = None):

    #frame = inspect.stack()[1]
    #module = inspect.getmodule(frame[0])
    #filename = module.__file__
    #filename = frame[0].f_code.co_filename

    frame = stack()[1]
    #calling_file = frame[0].f_code.co_filename
    calling_file = str(stack()[1][1].split("/")[-1])
    call_line_no = stack()[1][2]
    call_function = stack()[1][3]
    call_line_txt = stack()[1][4]

    #calling_file = str(__file__.split("/")[-1])
    #title = f"[ {calling_file} : {str(currentframe().f_back.f_lineno)} ]"
    #title = f"[ {calling_file} : {call_function} : {str(currentframe().f_back.f_lineno)} ]"
    title_info = f"[ {calling_file} : {call_function} : {call_line_no} ] ( {title} )"
    project_time = invoke(".Administrator", "Administration.Directors").time_code()
    #project_time = time_code()


    if headder == "headder":
        title_info = f"[ {project_name}, {__release__}/{__version__} ] :: ( {project_time} ) :: < Enter >"
        #return invoke(".Typographer", "Utilities.Maintenance").headding_section(
        return headding_section(
            marker=None, title=title_info
        )
    if headder == "footer":
        title_info = f"[ {project_name}, {__release__}/{__version__} ] :: ( {project_time} ) :: < Exit >"
        #return invoke(".Typographer", "Utilities.Maintenance").headding_section(
        return headding_section(
            marker=None, title=title_info
        )
    if headder == "section":
        #return invoke(".Typographer", "Utilities.Maintenance").headding_section(
        return headding_section(
            marker="-", title=title_info
        )




# Python program to print
# colored text and background
def print_format_table():
    colorama.init(autoreset=True)

    print('\033[31m' + 'some red text')
    print('\033[39m')  # and reset to default color
    print()
    print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}O{Fore.MAGENTA}R{Fore.CYAN}S{Fore.WHITE}!")
    print(f"{Fore.RED}Red Text")
    print(f"{Fore.GREEN}Green Text")
    print(f"{Fore.YELLOW}Yellow Text")
    print(f"{Fore.BLUE}Blue Text")
    print(f"{Fore.MAGENTA}Magenta Text")
    print(f"{Fore.CYAN}Cyan Text")
    print(f"{Fore.WHITE}White Text")
    print()
    print(f"{Back.RED}B{Back.GREEN}A{Back.YELLOW}C{Back.BLUE}K{Back.MAGENTA}G{Back.CYAN}R{Back.WHITE}O{Back.RED}U{Back.GREEN}N{Back.YELLOW}D{Back.BLUE}!")
    print(f"{Back.RED}Red Background")
    print(f"{Back.GREEN}Green Background")
    print(f"{Back.YELLOW}Yellow Background")
    print(f"{Back.BLUE}Blue Background")
    print(f"{Back.MAGENTA}Magenta Background")
    print(f"{Back.CYAN}Cyan Background")
    print(f"{Back.WHITE}White Background")
    print()
    print(f"{Style.DIM}S{Style.NORMAL}T{Style.BRIGHT}Y{Style.DIM}L{Style.NORMAL}E{Style.BRIGHT}!")
    print(f"{Style.DIM}Dim Text")
    print(f"{Style.NORMAL}Normal Text")
    print(f"{Style.BRIGHT}Bright Text")
    print()
    print(f"{Fore.YELLOW}{Back.RED}C{Back.GREEN}{Fore.RED}O{Back.YELLOW}{Fore.BLUE}M{Back.BLUE}{Fore.BLACK}B{Back.MAGENTA}{Fore.CYAN}I{Back.CYAN}{Fore.GREEN}N{Back.WHITE}A{Back.RED}T{Back.GREEN}I{Back.YELLOW}O{Back.BLUE}N")
    print(f"{Fore.GREEN}{Back.YELLOW}{Style.BRIGHT}Green Text - Yellow Background - Bright")
    print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}Cyan Text - White Background - Dim")
    print()
 
    print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}Cyan Text - White Background - Dim")


'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''


#import sys
def tcolor():
    #text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    #print(text)
    #cprint('Hello, World!', 'green', 'on_red')

    #print_red_on_cyan = lambda x: cprint('X', 'red', 'on_cyan')
    #print_red_on_cyan('Hello, World!')
    #print_red_on_cyan('Hello, Universe!')

    #for i in range(10):
        #cprint(i, 'magenta', end=' ')

    #c print("Attention!", 'red', attrs=['bold'], file=sys.stderr)
    colorscheme = {
        'Fore' : ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
        'Back' : ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white'],
        'Style': ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
        }
    marks = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    #res = len(max(colorscheme['Fore'], key = len))
    print(f"    ", end = '')
    print(f"{' ' * len(max(colorscheme['Fore'], key = len)) + ' '}", end = "")
    for color in colorscheme['Fore']:
        #append = ' ' * (11 - len(color))
        if len(color) < 8:
            append = ' ' * ( 8 - len(color))
            append = append + '  '
        cprint(f"{color}{append}", color, attrs=['bold'], end = " ")
        appen = ''
    print(f"")
    for back_ground in colorscheme['Back']:
        count = 0
        append = ' ' * (10 - len(back_ground))
        #print(f"{back_ground}{append}", end = " ")
        cprint(f"{back_ground}{append}",'white', back_ground, attrs=['bold'], end = "  ")
        while count < len(colorscheme['Fore']):
            #for check in marks:
            for style in colorscheme['Style']:
                cprint(f"X",colorscheme['Fore'][count], back_ground, attrs=[style], end = "")
            cprint(f"X",colorscheme['Fore'][count], back_ground, attrs=[colorscheme['Style'][0], colorscheme['Style'][5]], end = "")
            cprint(f"X",colorscheme['Fore'][count], back_ground, attrs=[colorscheme['Style'][0], colorscheme['Style'][4]], end = "")
            count += 1
            print(f"  ", end = " ")
        print(f"")



    #print(f"\n")
