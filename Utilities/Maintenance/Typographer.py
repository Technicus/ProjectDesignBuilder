# Typographer.py
# 2022.04.20.21.57

from os import get_terminal_size
from inspect import currentframe, stack
from os import system
from importlib import import_module as invoke
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
        marker = '═'
        #headding_prefix = '\n='
        headding_prefix = marker
        line_difference = 2
    else:
        #headding_prefix = '\n--'
        headding_prefix = marker * 2
        line_difference = 3
    terminal_size = get_terminal_size()
    if title == None:
        working_file = __file__.split('/')
        #title = f"┤ {working_file} ├┤{str(currentframe().f_back.f_lineno)} ├"
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
#═
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
            marker="─", title=title_info
            #marker="-", title=title_info
        )
