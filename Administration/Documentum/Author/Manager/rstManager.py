#!/bin/python

#$> clear; ./rstManager.py False

from sys import path as sysPath, argv
from os import walk, path, getcwd, system
#from os import system
#from sys import argv

#sys.path.insert(0, os.path.abspath('../../ProjectDesignBuilder/Directors'))
#rootProjectDesignBuilder = '../../ProjectDesignBuilder/'
#for directory in os.scandir(rootProjectDesignBuilder):
    #if directory.is_dir():
        ##print(directory.path)
        #sys.path.append(directory.path)


#if(len(argv) > 1 and argv[1] == True):
    #overwrite = True
#else:
    #overwrite = False


#overwrite = argv[1]
overwrite = bool(argv[1]) if len(argv) > 1 and argv[1] == str(True) else False

##overwrite = argv[1] if len(argv) > 1 and argv[1] == True True else False
if(overwrite == True):
    #print('\nOverwrite must be True.')
    print("overwrite:\n=========\n{}".format(overwrite))
else:
    #print('\nOverwrite must be False.')
    print("overwrite:\n=========\n{}".format(overwrite))

def agentQuery():
    agentQuery_List = open("agentQuery.list", "w")
    dirRoot = '../'
    dirCurrent = getcwd()
    head_tail = path.split(getcwd())
    dirWorking = head_tail[0]
    pathBase = path.basename(getcwd())
    dirProject = path.split(dirWorking)
    dirProject = path.join(dirProject[0], 'ProjectDesignBuilder')

    system(('cleanpy --all -v {}').format(dirProject))

    print("\nRelative:\n=========\n{}".format(dirRoot))
    print("\nCurrent:\n========\n{}".format(dirCurrent))
    print("\nWorking:\n========\n{}".format(dirWorking))
    print("\nBase:\n=====\n{}".format(pathBase))
    print("\nProject:\n========\n{}".format(dirProject))
    print("\nSystem Path Initialized:\n========================\n{}".format(sysPath))
    print("\nAgent Querry:\n====================")
    for agentLead, dirs, files in walk(dirProject, topdown=True):
        for agent in files:
            #print(path.join(dirRoot, name))
            agentFile = path.join(agentLead, agent)
            agent_split = path.split(agentFile)
            agentPath = agent_split[0]
            agentPath_split = path.split(agentPath)
            agentLeader = agentPath_split[1]
            #print('agent :: {}\n-------------'.format(agent))
            #print('[ agentFile ]\n(\'{}\')'.format(agentFile))
            #print('[ agentPath ]\n(\'{}\')\n'.format(agentPath))

            agentQuery_List = open("agentQuery.list", "a")
            agentQuery_List.write('{}\n'.format(agentLeader))
            agentQuery_List.write('{}\n\n'.format(agent))
            #agentQuery_List.write('agentLeader\n{}\n'.format(agentLeader))
            #agentQuery_List.write('agentFile\n{}\n'.format(agentFile))
            #agentQuery_List.write('agentPath\n{}\n\.'.format(agentPath))
            agentQuery_List.close()

        for agent in dirs:
            #if(name != '__pycache__'):
            dirWorkingAbs = path.join(agentLead, agent)
            sysPath.append(dirWorkingAbs)

            agentFile = dirWorkingAbs

            agent_split = path.split(agentFile)
            agentPath = agent_split[0]

            agentPath_split = path.split(agentPath)
            agentLeader = agentPath_split[1]

            #print('agent :: {}\n-------------'.format(agent))
            #print('[ agentPath ]\n(\'{}\')'.format(agentPath))
            #print('[ agentLead ]\n(\'{}\')\n'.format(agentLead))
            agentQuery_List = open("agentQuery.list", "a")
            #agentQuery_List.write('[ {} ]\n'.format(agent))
            agentQuery_List.write('{}\n'.format(agentLeader))
            agentQuery_List.write('{}\n\n'.format(agent))
            #agentQuery_List.write('( agentFile )\n{}\n'.format(agentFile))
            #agentQuery_List.write('( agentPath )\n{}\n'.format(agentPath))
            #agentQuery_List.write('( agentLeader )\n{}\n\n'.format(agentLeader))
            agentQuery_List.close()

    #print("\nSystem Path Update:\n===================\n{}".format(sysPath))
    #print("\nCurrent Directory:\n==================\n[\'{}\']".format(dirCurrent))

    #open and read the agent.list file after the appending:
    agentQuery_List = open("agentQuery.list", "r")
    #print('\n{}'.format(agentQuery_List.read()))
    agentQuery_List.close()
    print('agentQuery.list\n')
    return 0


def agentCoalation():
    print("Agent Report:\n====================")

    agentQuery_List = open("agentQuery.list", "r")
    Lines = agentQuery_List.readlines()
    agentQuery_List.close()

    countLine = -1
    countAgent = 0
    counterAgent = 0
    deliminator = ';'
    agentReport = ['', '']
    agentReportCount = 0
    agentTotal = 0
    agentReport_List = open("agentReport.list", "w")
    agentReport_List.write('countField;agentStatus;agentTitle;agentHeadding;agentAuxiliumStatus;agentAuxilium;agentAuxiliumHeadding\n'.format())
    agentReport_List.close()
    # Strips the newline character
    for line in Lines:
        countLine += 1
        currentLine = line.strip()
        agentLength = len(currentLine)
        if(agentLength != 0):
            if(counterAgent < 2):
                counterAgent += 1
            else:
                countAgent += 1
                counterAgent = 1

            if "."  not in currentLine:
                agentType = 'Support'
            else:
                agentType = 'Lead'
            #print('{} : {}'.format(agentReportCount, currentLine))
            if( currentLine == 'ProjectDesignBuilder'):
                agentType = 'Chief'
                #print('Chief AGENT :: {}'.format(currentLine))
                #print("Line{} : {} : {} : {} : {}".format(countLine, countAgent, currentLine, agentLength, agentType))
                #agentReport[0] = str(countAgent) + deliminator + agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                #agentReport[agentReportCount] = str(countAgent) + deliminator + agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                agentReport[agentReportCount] = agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                #agentReport[agentReportCount] = agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                # print ('[ agentReport : {} ]( {} )'.format(agentReportCount, agentReport[agentReportCount]))
                #agentReportCount += 1
            else:
                #agentType = 'Support'
                #print("Line{} : {} : {} : {} : {}".format(countLine, countAgent, currentLine, agentLength, agentType))
                #print ('[ agentReport : {} ]( {} )'.format(agentReportCount, agentReport[0]))
                #print ('[ agentReport : {} ]( {} )'.format(agentReportCount, agentReport[0]))

                if(agentReportCount == 0):
                    #agentReport[agentReportCount] = str(countAgent) + deliminator + agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                    agentReport[agentReportCount] = agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                    #agentReport[agentReportCount] = agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                    # print ('[ agentReport : {} ]( {} )'.format(agentReportCount, agentReport[agentReportCount]))
                    #agentReportCount += 1
                    #if(agentReportCount < 1):
                        #agentReportCount += 1
                    #else:
                        #agentReportCount = 0
                else:
                    #agentReport[agentReportCount] = str(countAgent) + deliminator + agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                    agentReport[agentReportCount] = agentType + deliminator + str(currentLine) + deliminator + str(agentLength)
                    # print ('[ agentReport : {} ]( {} )'.format(agentReportCount, agentReport[agentReportCount]))
                    #agentReportCount += 1
                    #if(agentReportCount < 1):
                        #agentReportCount += 1
                    #else:
                        #agentReportCount = 0

                    #print ('[ {} ]( {} ) & ( {} )'.format(countAgent, agentReport[0], agentReport[1]))

                    agentReport_List = open("agentReport.list", "a")
                    agentReport_List.write('{};{};{}\n'.format(countAgent, agentReport[0], agentReport[1]))
                    agentReport_List.close()

            if(agentReportCount == 0):
                agentReportCount += 1
            else:
                agentReportCount = 0
    print('agentReport.list\n')
    return 0

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def agentRestructure():
    print("Agent Restructure:\n====================\n")

    agentReport_List = open("agentReport.list", "r")
    agentData = agentReport_List.readlines()
    agentReport_List.close()
    agentStructure_List = open("agentStructure.list", "w")
    agentStructure_List.close()

    agentLine = 1
    agentStructure = [{
       'agentTitle' : ['','\n'],
       'agentTOC' : '\n.. toctree::\n   :maxdepth: 2\n',
       'agentParent' : [''],
       'agentChilds' : ['']
    }]
    for line in agentData:
        agentStructure.append({
       'agentTitle' : ['','\n'],
       'agentTOC' : '\n.. toctree::\n   :maxdepth: 2\n',
       'agentParent' : [''],
       'agentChilds' : ['']
        })
        agentLine += 1

    agentLine = 1
    countAgent = 0
    counterAgent = 0
    agentQue = ['', '']
    #flags = { 'Chief' : False }
    agentflags = { }
    agentQue = ['', '']
    for line in agentData:
        agentField = agentData[agentLine].split(';')
        agentStatus = agentField[1]
        agentTitle = [agentField[2], '']
        agentHeadding = ''
        for headding in range(0, len(agentTitle[0])):
            agentHeadding = agentHeadding + '='
        agentTitle = [agentField[2], agentHeadding]
        agentAuxilium = [agentField[5], agentField[6][:-1]]
        agentQue[counterAgent] = agentTitle[0]

        if agentStatus not in agentflags:
            agentflags[agentStatus] = False
            print('Add flag : {} = {}'.format(agentStatus, agentflags[agentStatus]))
        if(agentTitle[0] == 'ProjectDesignBuilder'):
            if(agentflags['Chief'] == False):
                print()

        if(agentflags['Chief'] == False):
            #print('?')
            agentflags[agentStatus] = True
            print('agentStatus : {}'.format(agentStatus))
            print('agentflags : {} = {}'.format(agentStatus, agentflags[agentStatus]))

            agentStructure_List = open("agentStructure.list", "a")
            #agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTitle'][0]))
            #agentStructure_List.write('{}\n'.format(agentName))
            #agentStructure_List.write('{}\n\n'.format(agentHeadding))
            #agentTitle = [agentName, agentHeadding]
            agentStructure[agentLine]['agentTitle'][0] = agentTitle[0] #+ '\n' + agentHeadding
            agentStructure[agentLine]['agentTitle'][1] = agentTitle[1]
            agentStructure[agentLine]['agentTOC'] = '\n.. toctree::\n   :maxdepth: 2'
            agentStructure[agentLine]['agentParent'] = agentAuxilium
            agentStructure[agentLine]['agentChilds'] = agentAuxilium

            #agentStructure_List = open("agentStructure.list", "a")

            #print('{}\n{}'.format(agentStructure[agentLine]['agentTitle'][0], agentStructure[agentLine]['agentTitle'][1]))
            agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTitle'][0]))
            agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTitle'][1]))
            agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTOC']))
            #agentStructure_List.write('\n   {}\n'.format(agentStructure[agentLine]['agentParent']))
            agentStructure_List.close()

        #print(counterAgent, countAgent, str(agentQue))
        #if(agentQue[counterAgent] == agentQue[countAgent]):
        #if(agentQue[counterAgent] == agentAuxilium):
            #print(counterAgent, countAgent, str(agentQue))
            #print(str(agentAuxilium[0]))
            #agentStructure_List = open("agentStructure.list", "a")
            #agentStructure_List.write('\n    {}'.format(str(agentAuxilium[0])))
            #agentStructure_List.close()





        agentLine += 1
        if(counterAgent == 0):
            counterAgent += 1
            countAgent = 0
        else:
            counterAgent = 0
            countAgent += 1

        #agentField[6] = agentField[6][:-1]
        #print('agentField report:\n {}'.format(agentField[agentLine]))
        #print('agentStatus : {}'.format(agentStatus))
        #print('flag : {}'.format(flags[agentStatus]))

        #print('Flags keys = {}'.format(flags.keys()))

        #print('agentField[{}] = {}'.format(agentLine, agentField))
        #print('{} | {} | {} | {}'.format(agentStatus, agentName, agentHeadding, agentSupport))
        #print('{} | {} | {}'.format(agentStatus, agentName, agentSupport))
        #print('{}\n{}\n\n{}\n'.format(agentStatus, agentName, agentHeadding, agentSupport))
        #agentType = '.split(';')'

        #print('agentStatus ')
        #print('{}'.format(agentField[1]))
        #if(agentField[1] == 'Chief'):
        #if(agentField[agentLine] in flags.keys()):
        #if(flags[agentStatus] == False):

            #print('Flag value is {}'.format(flags[agentField[agentLine]]))
            #print('Flags keys = {}'.format(flags.keys()))
            #print('Flags = {}\n'.format(flags))
            #print('{}'.format(flags['Chief']))
            #if (flags['Chief'] == False):
                #flags['Chief'] = True
                ##print('{}'.format(flags['Chief']))
                #print('{} | {} | {}'.format(agentStatus, agentName, agentSupport))




        #if(agentField[1] == 'Support'):
            ##print('{}'.format(agentField[1]))
            #print('{} | {} | {}'.format(agentStatus, agentName, agentSupport))


        #agentTitle = [agentName, agentHeadding]
        #agentSupports = agentSupport
        #agentStructure[agentLine]['agentTitle'][0] = agentName #+ '\n' + agentHeadding
        #agentStructure[agentLine]['agentTitle'][1] = agentHeadding
        #agentStructure[agentLine]['agentTOC'] = '\n.. toctree::\n   :maxdepth: 2'
        #agentStructure[agentLine]['agentParent'] = agentSupport
        #agentStructure[agentLine]['agentChilds'] = agentSupports

        #agentStructure_List = open("agentStructure.list", "a")

        ##print('{}\n{}'.format(agentStructure[agentLine]['agentTitle'][0], agentStructure[agentLine]['agentTitle'][1]))
        #agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTitle'][0]))
        #agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTitle'][1]))
        #agentStructure_List.write('{}\n'.format(agentStructure[agentLine]['agentTOC']))
        #agentStructure_List.write('\n   {}\n'.format(agentStructure[agentLine]['agentParent']))
        #agentStructure_List.write('   {}\n\n\n'.format(agentStructure[agentLine]['agentChilds']))

        #agentStructure_List.close()

    print()


    #print('Total Matched lines : ', len(matched_lines))
    #for elem in matched_lines:
    #print('Line Number = ', elem[0], ' :: Line = ', elem[1])

    #print('agentRrestructure.?\n')
    return 0



agentQuery()
agentCoalation()
agentRestructure()


        #print('{} | {}'.format(agentReport[0], agentReport[1]))


# agent.rst
#ProjectDesignBuilder
#====================
        #count += 3
        #agentLength = len(currentLine)
        #print('agentLength = {}'.format(agentLength))

#.. toctree::
   #:maxdepth: 2

   #Utility
