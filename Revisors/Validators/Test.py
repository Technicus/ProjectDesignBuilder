##!/bin/python

#__version__ = "0.0.1"
#__subvision__ = "Test.py"
#__title__ = "Test Builder"
#__subTitle__ = "Customizable Tester"
#__author__ = "Technicus"

#import cadquery as cq
#from cadquery import exporters
#import sys

## Main function
##def main(createExport = False):
#def main(export = False):
    #log('---- main() ----')
    ##Build the bottom and top panels
    ##Design parameters
    #width = 10
    #height = 10
    #depth = 5
    #box_00 = cq.Workplane("XY")
    #box_00 = box_00.box(10.0, 10.0, 5)
    #box_01 = box_00.translate((5.0,5.0))
    #box_02 = box_00.translate((-5.0,-5.0))
    #box_03 = box_00.intersect(box_01)
    #box_04 = box_00.intersect(box_02)
    #box_05 = box_03.intersect(box_04)
    #show_object(box_05)
    ##show_object(box_00)
    ##show_object(box_01)
    ##show_object(box_02)
    ##show_object(box_03)
    ##show_object(box_04)

    #highlight_00 = box_00.faces('>Z')
    ##highlight_01 = box_01.faces('>Z')
    ##show_object(highlight_00,'highlight',options=dict(alpha=0.1,color=(1.,0,0)))
    ##show_object(highlight_01,'highlight',options=dict(alpha=0.1,color=(1.,0,0)))

    ## Render or export
    ##if createExport == True:
        ##exporters.export(box_00, './box.step')
    ##else:
        ##createExport = False
        ##print('__name__ : {}'.format(__name__))

        ##log('ex[prt to box.step')
        ##result = cq.Workplane().box(10, 10, 10)
        ##highlight = result.faces('>Z')
        ##exporters.export(highlight, './box.step')

        ##show_object(result)
        ##show_object(highlight,'highlight',options=dict(alpha=0.1,color=(1.,0,0)))
        ##print('__name__ : {}'.format(__name__))
        ##print('d : {}'.format(__name__))

#if __name__ == "__main__":
    #main(False)

#if __name__ == 'temp':
    ##argument = sys.argv[1]
    #log('---- cq-editor ----')
    ##testVariable = sys.argv[1]
    #log('what{}'.format(__name__))
    ##log('argv[1]  : {}'.format(argument))
    ##print('__name__ : {}'.format(__name__))
    ##print('d : {}'.format(__name__))
    #main()


    ##print('{}'.format(__name__))
    ##print("\nMain will start.\n")
    ##print("Main is on.\n")
    ##print("Main is done.\n")