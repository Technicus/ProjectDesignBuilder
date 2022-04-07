#!/bin/python

__version__ = "0.0.1"
__subvision__ = "Design.py"
__title__ = "Design Builder"
__subTitle__ = "Customizable Crafting System"
__author__ = "Technicus"

# This is a file to design a customizable organizer, and create parts for laser cut out and assembly.


from sys import path as sysPath
from os import walk, path, getcwd

dirRoot = '../'
dirCurrent = getcwd()
head_tail = path.split(getcwd())
dirWorking = head_tail[0]
pathBase = path.basename(getcwd())
print("\nBase Path:\n{}".format(dirWorking))
print("\nSystem Path Initialized:\n{}".format(sysPath))
print("\nWorking Path Querry:")
for dirWorking, dirs, files in walk(dirWorking, topdown=True):
    #for name in files:
        #print(path.join(dirRoot, name))
    for name in dirs:
        if(name != '__pycache__'):
            dirWorkingAbs = path.join(dirWorking, name)
            print("[\'{}\']".format(dirWorkingAbs)) # Absolute
            sysPath.append(dirWorkingAbs)
print("\nSystem Path Update:\n{}".format(sysPath))
print("\nCurrent Directory:\n[\'{}\']".format(dirCurrent))

#from datetime import date, datetime
#import cadquery as cq
#from cadquery import exporters

from Utility import clear, setParameters, setDirectories
#from Craft import build
##from Construct import cabinet drawer
##from Export import showcase model
#import configparser

 #⦾••⦾
 #⦿⦾○◦•

# Main function
def main(argumentation = False):
    """ProjectDesignBuilder.main()"""
    # Clear the terminal
    #clear()
    print("\n⦿⦾•○◦ Main() Starts Here ◦○•⦾⦿\n")
    parameters = setParameters(report = True)
    parameterFile = setParameters(returnFile = True)
    #directories = setDirectories(report = True, parameterSet = parameters['Paths'])
    #build(craft = 'Cabinet', design = parameters['Design'])

    #Cabinet = build(craft = 'Cabinet', design = parameters['Design'])
    #build()
    ## Tab design
    #tabProportion = False
    #tabCount = 5
    #tabWidth = 1
    #tabSide = "Left"
     ## Variables to set dimentions, rows, colums, material thichness, and measurements for functions.
     ## Overall dimentions
     ## Material thicknesses
     ## [ cabinet, drawers ]
     #thicknessCabinetPanels = 6.0
     ## Rows and colums
     ## [ rows, columns ]
     #grid = [ 14.0, 10.0 ]
     #drawerWidth = 125.0 / 3
     ## [ width, height, _depth ]
     ##cabinetDimention = [ 600.0, 250.0, 125.0 ]
     #DrawerDimention = [ drawerWidth, drawerWidth, drawerWidth * 8 ]
     #cabinetDimention = [ DrawerDimention[ 0 ] * grid[ 0 ], DrawerDimention[ 1 ] * grid[ 1 ], DrawerDimention[ 2 ] + thicknessCabinetPanels ]

     ## Distribution
     ## [ columnWidth =  width / columns, rowHeight = height / rows ]
     #gridDistribution = [ cabinetDimention[ 0 ] / grid[ 1 ], cabinetDimention[ 1 ] / grid[ 0 ] ]

     ## Tab configuration
     ## The tab count and width need to be recalculated to match the side proportionas
     ## [ count, tolerance, porportion, justification ]
     ## tabDefinition = [ 4, 1.0, 0.5, "Centered" ]
     #tabCount = 7
     #tabTolerance = 1.0
     #tabPorportion = 1.0
     #tabJustification = "Centered"
     #tabInset = 0

     #show_object(panelAssembly)
     ##show_object(panelBottom)
     ##show_object(panelLeft)
     ##show_object(panelBack)
         ##exporters.export(panelAssembly, 'cabinet.step')
     #functionStatus()
     ## Instintantiate an object with initial settings condition
     ## by parsing the arguments, parsing the config file, referencing defaults, and establishing a directory reference
     ##print("> Function call: Utility = initalize_Utility()")
     #Utility = initalize_Utility()
     ##functionStatus()
     ## Display version information
     ##print("> Function call: version(Utility)")
     #version(Utility)
     ##functionStatus()
     #evaluateOperations(Utility)
    print("\n⦿⦾•○◦ Main() Ends Here ◦○•⦾⦿\n")

if __name__ == "__main__":
    main(False)

#if __name__ == 'temp':
    ##clear()
    ##argument = sys.argv[1]
    #log('---- cq-editor ----')
    ##testVariable = sys.argv[1]
    #log('what{}'.format(__name__))
    ##log('argv[1]  : {}'.format(argument))
    ##print('__name__ : {}'.format(__name__))
    ##print('d : {}'.format(__name__))
    #print("\n⦿⦾•○◦ Transfering to Main() ◦○•⦾⦿\n")
    #main()

