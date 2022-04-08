




## Create tab sketches
## Sketch for X tabs
#tabWidth = cabinetDimention[ 2 ] / tabCount
#sketchTabsX = cq.Sketch()
#sketchTabsX = sketchTabsX.rarray( tabWidth, 1, int( tabCount ), 1 )
#sketchTabsX = sketchTabsX.rect(( cabinetDimention[ 2 ] / tabCount ) / 2, thicknessCabinetPanels )

## Sketch for Y tabs
#tabCountY = (( cabinetDimention[ 0 ] / tabWidth / 2 ) * 2 ) - 1
#sketchTabsY = cq.Sketch()
#sketchTabsY = sketchTabsY.rarray( tabWidth, 1, int( tabCountY ), 1 )
#sketchTabsY = sketchTabsY.rect( tabWidth / 2, thicknessCabinetPanels )

## Sketch for Y0 tabs
#tabCountY = (( cabinetDimention[ 2 ] / tabWidth / 2 ) * 2 ) - 1
#sketchTabsY0 = cq.Sketch()
##sketchTabsY0 = sketchTabsY0.rarray( 1, tabWidth, 1, int( tabCountY + 2 ))
##sketchTabsY0 = sketchTabsY0.rect( thicknessCabinetPanels, tabWidth / 2 )
#sketchTabsY0 = sketchTabsY0.rarray( tabWidth, 1, int( tabCountY + 2 ), 1 )
#sketchTabsY0 = sketchTabsY0.rect( tabWidth / 2, thicknessCabinetPanels )

## Sketch for Z tabs
#tabCountZ = (( cabinetDimention[ 1 ] / tabWidth / 2 ) * 2 ) - 1
#sketchTabsZ = cq.Sketch()
##sketchTabsZ = sketchTabsZ.rarray( tabWidth, 1, int( tabCountZ ), 1 )
##sketchTabsZ = sketchTabsZ.rarray( 1, tabWidth, 1, int( tabCountZ ) )
##sketchTabsZ = sketchTabsZ.rect( thicknessCabinetPanels, tabWidth / 2 )
#sketchTabsZ = sketchTabsZ.rarray( tabWidth, 1, int( tabCountZ + 2 ), 1 )
#sketchTabsZ = sketchTabsZ.rect( tabWidth / 2, thicknessCabinetPanels )

## Sketches for back panel

##--- More code needed here

## Establish dimentions for panels
## The bottom and left panels are going to be mirrored to create the top and right panels.
## The horizontal panels will be cut and transformed into an array.
#panelDimentionBottom = [cabinetDimention[ 0 ], cabinetDimention[ 2 ], thicknessCabinetPanels ]
#panelDimentionLeft = [cabinetDimention[ 1 ], cabinetDimention[ 2 ], thicknessCabinetPanels ]
#panelDimentionBack = [cabinetDimention[ 0 ], cabinetDimention[ 1 ], thicknessCabinetPanels ]
## The horizontal panels will be cut and transformed into an array.
#verticalSeperator = [cabinetDimention[ 1 ], cabinetDimention[ 2 ], thicknessCabinetPanels ]
#horizontalSeperator = [cabinetDimention[ 0 ], cabinetDimention[ 2 ], thicknessCabinetPanels ]

##--- More code needed her






















## Define panels for hull
## Build the bottom and top panels
#panelBottom = cq.Workplane("XY")
#panelBottom = panelBottom.box(panelDimentionBottom[ 0 ], panelDimentionBottom[ 1 ], panelDimentionBottom[ 2 ]  )

## Cut tabs on ">X"
#panelBottom = panelBottom.faces(">X").tag("bottom_a")
#panelBottom = panelBottom.workplane(origin=( 0, 0 ))
#panelBottom = panelBottom.placeSketch(sketchTabsX)
#panelBottom = panelBottom.extrude( -thicknessCabinetPanels, combine="cut" )

## Cut tabs on "<X"
#panelBottom = panelBottom.faces("<X").tag("bottom_b")
#panelBottom = panelBottom.workplane(origin=( 0, 0 ))
#panelBottom = panelBottom.placeSketch(sketchTabsX)
#panelBottom = panelBottom.extrude( -thicknessCabinetPanels, combine="cut" )

## Cut tabs on "<Y"
#panelBottom = panelBottom.faces("<Y").tag("bottom_c")
#panelBottom = panelBottom.workplane(origin=( 0, 0 ))
#panelBottom = panelBottom.placeSketch(sketchTabsY)
#panelBottom = panelBottom.extrude( -thicknessCabinetPanels, combine="cut" )

## Place the bottom panel
##panelBottom = panelBottom.translate(( 0, 0, (-cabinetDimention[ 1 ] / 2 ) + (panelDimentionBottom[ 2 ] / 2 )))

## Create a mirrorr of panelBottom for panelTop
#panelTop = panelBottom.mirror(mirrorPlane = "XY", basePointVector = ( 0, 0, 0 ))
#panelTop = panelTop.translate(( 0, 0, (cabinetDimention[ 1 ] / 2 ) + (panelDimentionBottom[ 2 ] / 2 )))
## panelTop = panelBottom()
## panelsTopAndBottom = panelBottom.union(panelTop)

## Create panelTop tags
#panelTop.faces( ">Z" ).tag( "ptZ" )

## Build left panel
#panelLeft = cq.Workplane( "XY" )
#panelLeft = panelLeft.box( panelDimentionLeft[ 0 ], panelDimentionLeft[ 1 ], panelDimentionLeft[ 2 ] )

## Cut tabs on ">Y"
#panelLeft = panelLeft.faces(">X").tag("left_a")
#panelLeft = panelLeft.workplane(origin=( 0, 0 ))
#panelLeft = panelLeft.placeSketch(sketchTabsY0)
#panelLeft = panelLeft.extrude( -thicknessCabinetPanels, combine="cut" )

## Cut tabs on ">Y"
#panelLeft = panelLeft.faces("<X").tag("left_b")
#panelLeft = panelLeft.workplane(origin=( 0, 0 ))
#panelLeft = panelLeft.placeSketch(sketchTabsY0)
#panelLeft = panelLeft.extrude( -thicknessCabinetPanels, combine="cut" )
##panelLeft = panelLeft.extrude( -thicknessCabinetPanels )

## Cut tabs on "<Z"
#panelLeft = panelLeft.faces("<Y").tag("left_c")
#panelLeft = panelLeft.workplane(origin=( 0, 0 ))
#panelLeft = panelLeft.placeSketch(sketchTabsZ)
#panelLeft = panelLeft.extrude( -thicknessCabinetPanels, combine="cut" )
##panelLeft = panelLeft.extrude( -thicknessCabinetPanels )

## Create tags for panelLeft faces
##panelLeft.faces( ">Y" ).tag( "plY" )
## Rotate and translate left panel
##panelLeft = panelLeft.rotateAboutCenter(( 1, 0, 0 ) ,90 )
##panelLeft = panelLeft.translate((( cabinetDimention[ 0 ] / 2) - ( panelDimentionLeft[ 2 ] / 2 ), 0, 0 ))

## Create a mirrorr of panelLeft panel for panelRight
#panelRight = panelLeft.mirror(mirrorPlane = "XY", basePointVector = ( 0, 0, 0 ))
##panelRight = panelLeft().translate( 0, 0, 0)

## Build back panel
#panelBack = cq.Workplane( "XY" )
#panelBack = panelBack.box( panelDimentionBack[ 0 ], panelDimentionBack[ 1 ], panelDimentionBack[ 2 ] )
##panelBack = panelBack.translate((0, -1 * (cabinetDimention[2] / 2) + (panelDimentionBack[2] / 2), 0))
