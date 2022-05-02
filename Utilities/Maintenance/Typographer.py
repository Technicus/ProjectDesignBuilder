# Typographer.py
# 2022.04.20.21.57

from os import get_terminal_size
from inspect import currentframe, stack
from os import system
#from importlib import import_module as invoke
#from inspect import currentframe  # , getframeinfo, trace


def clear():
    """This function only has support to clear the screen for Linux of Mac."""
    _ = system("clear")


def headding_section(marker = None, title = None, subtitle = None):
    """This funciton returns a section for printing to console or adding
    to logs to seperate process for improving readability.  It also
    provides some process information.  This can be improved with more
    development of process_inspection()."""
    terminal_size = get_terminal_size()
    if marker is None:
        marker = '═'
        #headding_prefix = '\n='
        headding_prefix = f"╞{marker}"
        headding_suffix = f"{marker}╡"
        line_difference =  4
    else:
        #headding_prefix = '\n--'
        headding_prefix = f"├{marker * 1}"
        headding_suffix = f"{marker * 1}┤"
        line_difference = 4
    if title is None:
        #working_file = __file__.split('/')
        #title = f"┤ {working_file} ├┤{str(currentframe().f_back.f_lineno)} ├"
        #title = f"[ {working_file} ] : {str(currentframe().f_back.f_lineno)} ]"
                #len(working_file[-1]) - 11 )
        title = ''
    else:
        title = f"[ {title} ]"
    if subtitle is None:
        subtitle = ''
    else:
        subtitle = f"( {subtitle} )"

        #marker = marker * (terminal_size.columns - len(title) - len(subtitle) - line_difference)
    long_marker = marker * (terminal_size.columns - len(title) - len(subtitle) - line_difference)
    section = f"{headding_prefix}{title}{long_marker}{subtitle}{headding_suffix}"
    return section


def section(headder='section', title = None, subtitle = None, trace_frame = False):
    """Section is intended for drawing a line across the terminal with intetnt
    to signify beginning or end of a process series.  The original idea was to
    automatically include debugging information into the headder.  Debug
    features are not yet properly developed.  section() and headding_section()
    are mutual dependants."""
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
    if trace_frame:
        #subtitle = f"[ {calling_file} : {call_function} : {call_line_no} ] ( {title} )"
        #project_time = invoke(".Administrator", "Administration.Directors").time_code()
        #title = f"[ {project_name}, {__release__}/{__version__} ] :: ( {project_time} )"
        subtitle = f"{calling_file} : {call_function} : {call_line_no}"
    #if subtitle == None:
        #subtitle = ''
    if headder == "headder":
        return headding_section(
            marker=None, title=title, subtitle = subtitle
        )
    if headder == "footer":
        return headding_section(
            marker=None, title=title, subtitle = subtitle
        )
    if headder == "section":
        return headding_section(
            marker="─", title=title, subtitle = subtitle
        )


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


def draft_output(
        draft = None,
        output = 'compositor',
        layout = None,
        derivative = None):
    """draft_output() is for preparing strings to be sent out for reports
    to the console, logs, standard output, or whereverelse deemed.  From
    here the draft might go to the compositor for prosessing to a
    terminal maybe.  This mechanisim is still being developed."""
    if output == 'compositor':
        pass
    if output == 'console':
        print(f"{draft}")
    if output == 'log':
        pass
    if output == 'file':
        pass
    if output == '?':
        pass



