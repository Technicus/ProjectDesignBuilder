#!/bin/python
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

#import re
#import pathlib
from pathlib import Path as libPath

#regex = r"(\w+) = (\w+|\[[^\[\]]*\])"

#test_str = ("[\"project_path = None, project_path = None, directory_omit = ['.git', '__', 'html'], file_register_types = ['.md', '.py', '.rst', '.html', '.log', '.ini'], dictionary = {key0 : value, key1 : value}, tuple = (t, u, ple)\"]\n")

#matches = re.finditer(regex, test_str, re.MULTILINE)

#for matchNum, match in enumerate(matches, start=1):
    ##print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #print(f"{match.group()}")

    ##for groupNum in range(0, len(match.groups())):
        ##groupNum = groupNum + 1
        ##print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

## Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.



#filepath = pathlib.Path('.').glob('**/RegistryManager.py')
#print(dir(filepath))
#print(pathlib.PurePath(str(filepath).parts)

filepath = sorted(libPath('.').glob('**/RegistryManager.py'))
delim = '\''
#module = f"./{str(filepath).split(delim)[1]}"
module = str(filepath).split('\'')[1]
print(f"{module}")
module_name = f".{module.rsplit('/', 1)[1].strip('.py')}"
print(f"{module_name}")
module_path = module.rsplit('/', 1)[0]
print(f"{module_path}")



