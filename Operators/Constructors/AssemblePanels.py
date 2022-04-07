


## Create tags for panelAssembly
## Tagesfor panelTop
#panelTop.faces(">Y").tag("panelTop_FrontFace")
#panelTop.faces("<Z").tag("panelTop_UnderTab")
#panelTop.faces(">Y").edges("<Z").tag("panelTop_FrontBottomEdge")

## Tagesfor panelLeft
#panelTop.faces(">Y").edges(">X").tag("panelTop_FrontLeftEdge")
#panelTop.faces(">Y").edges(">X").vertices("<Z").tag("panelTop_FrontLeftBottomVert")

#panelLeft.faces(">Y").tag("panelLeft_FrontFace")
#panelLeft.faces(">Y").edges(">X").tag("panelLeft_FrontLeftTopEdge")
#panelLeft.faces(">Y").edges("<X").vertices(">Z").tag("panelLeft_FrontTopLeftVert")
#panelLeft.faces(">Y").edges("<X").vertices("<Z").tag("panelLeft_FrontTopRightVert")
#panelLeft.faces("<Y").edges("<X").vertices(">Z").tag("panelLeft_BackTopRightVert")
#panelLeft.faces("<X").tag("panelLeft_TopFrontUnderTab")

## Tagesfor panelRight
#panelTop.faces(">Y").edges("<X").tag("panelTop_FrontRightEdge")
#panelTop.faces(">Y").edges("<X").vertices("<Z").tag("panelTop_FrontRightBottomVert")

#panelRight.faces(">Y").tag("panelRight_FrontFace")
#panelRight.faces(">Y").edges(">X").tag("panelRight_FrontRightTopEdge")
#panelRight.faces(">Y").edges(">X").vertices("<Z").tag("panelRight_FrontTopLeftVert")
#panelRight.faces(">Y").edges(">X").vertices(">Z").tag("panelRight_FrontTopRightVert")
#panelRight.faces("<Y").edges(">X").vertices("<Z").tag("panelRight_BackTopRightVert")
#panelRight.faces(">X").tag("panelRight_TopFrontUnderTab")

## Tages for panelBottom
#panelBottom.faces(">Z").tag("panelBottom_TopFace")
#panelBottom.faces(">Y").edges(">X").vertices(">Z").tag("panelBottom_TopFrontLeftVert")
#panelBottom.faces(">Y").edges("<X").vertices(">Z").tag("panelBottom_TopFrontRightVert")
#panelBottom.faces("<Y").edges(">X").vertices(">Z").tag("panelBottom_TopBackLeftVert"  )
#panelBottom.faces("<Y").edges("<X").vertices(">Z").tag("panelBottom_TopBackRightVert" )

#panelLeft.faces( "<X[-2]").tag("panelLeft_BottomTabCut" )
#panelLeft.faces( ">Y").edges(">X").vertices(">Z").tag("panelLeft_BottomFrontLeftVert" )
#panelLeft.faces( "<Y[-2]").edges(">X").vertices("<Z").tag("panelLeft_BottomBackLeftVert")
#panelRight.faces(">Y").edges("<X").vertices(">Z").tag("panelRight_BottomBackLeftVert" )
#panelRight.faces("<Y").edges("<X").vertices("<Z").tag("panelRight_BottomBackRightVert")

## Tages for panelBack
#panelBack.faces(">Y").tag("panelBack_TopFace")
#panelBack.faces("<Y").tag("panelBack_BottomFace")
#panelBack.faces("<Y").tag("panelBack_LeftFace")
#panelBack.faces("<Y").tag("panelBack_RightFace")
#panelBack.faces(">Z").tag("panelBack_BackFace")
#panelBack.faces(">Y").edges("<Z").tag("panelBack_TopBackEdge")
#panelBack.faces("<Y").edges("<Z").tag("panelBack_BottomBackEdge")
#panelBack.faces(">X").edges("<Z").tag("panelBack_LeftBackEdge")
#panelBack.faces("<X").edges("<Z").tag("panelBack_RightBackEdge")
#panelBack.faces(">X").edges(">Y").vertices(">Z").tag("panelBack_TopBackLeftVert")
#panelBack.faces("<X").edges(">Y").vertices(">Z").tag("panelBack_TopBackRightVert")
#panelBack.faces(">X").edges("<Y").vertices(">Z").tag("panelBack_BottomBackLeftVert")
#panelBack.faces("<X").edges("<Y").vertices(">Z").tag("panelBack_BottomBackRightVert")

#panelTop.faces("<Z").tag("panelTop_TopFace")
#panelTop.faces("<Y").tag("panelTop_BackFace")
#panelBottom.faces("<Z").tag("panelBottom_BottomFace")
#panelLeft.faces("<Y").tag("panelLeft_LeftFace")
#panelRight.faces("<X").tag("panelRight_RightFace")

#panelTop.faces("<Y[-2]").edges(">Z").tag("panelTop_TopBackEdge")
#panelBottom.faces("<Y[-2]").edges("<Z").tag("panelBottom_BottomBackEdge")
#panelLeft.faces("<Y[-2]").edges(">Z").tag("panelLeft_LeftBackEdge")
#panelRight.faces("<Y[-2]").edges(">Z").tag("panelRight_RightBackEdge")

#panelBottom.faces("<Y").edges(">X").vertices("<Z").tag("panelBottom_TopBackLeftVert")
#panelBottom.faces("<Y").edges("<X").vertices("<Z").tag("panelBottom_TopBackRightVert")
#panelTop.faces("<Y").edges(">X").vertices(">Z").tag("panelTop_BottomBackLeftVert")
#panelTop.faces("<Y").edges("<X").vertices(">Z").tag("panelTop_BottomBackRightVert")

## Create the assembly and define the elements
#panelAssembly = cq.Assembly()
## Add solids to panelAssembly
#panelAssembly = panelAssembly.add( panelTop, name = "panelTop", color = cq.Color( "yellow" ))
#panelAssembly = panelAssembly.add( panelLeft, name = "panelLeft", color = cq.Color( "red" ))
#panelAssembly = panelAssembly.add( panelRight, name = "panelRight", color = cq.Color( "green" ))
#panelAssembly = panelAssembly.add( panelBottom, name = "panelBottom", color = cq.Color( "Blue" ))
#panelAssembly = panelAssembly.add( panelBack, name = "panelBack", color = cq.Color( "tan" ))
## Place panelTop
#panelAssembly.constrain("panelTop", "Fixed")
## Place panelLeft
#panelAssembly.constrain( "panelLeft?panelLeft_FrontTopLeftVert", "panelTop?panelTop_FrontLeftBottomVert", "Point" )
#panelAssembly.constrain( "panelLeft?panelLeft_FrontLeftTopEdge", "panelTop?panelTop_FrontBottomEdge", "Axis" )
#panelAssembly.constrain( "panelLeft?panelLeft_TopFrontUnderTab", "panelTop?panelTop_UnderTab", "Axis" )
## Place panelRight
#panelAssembly.constrain( "panelRight?panelRight_FrontTopRightVert", "panelTop?panelTop_FrontRightBottomVert", "Point" )
#panelAssembly.constrain( "panelRight?panelRight_FrontRightTopEdge", "panelTop?panelTop_FrontBottomEdge", "Axis" )
#panelAssembly.constrain( "panelRight?panelRight_TopFrontUnderTab", "panelTop?panelTop_UnderTab", "Axis" )
## Place panelBottom
#panelAssembly.constrain( "panelBottom?panelBottom_TopFrontLeftVert" , "panelLeft?panelLeft_BottomFrontLeftVert" , "Point" )
#panelAssembly.constrain( "panelBottom?panelBottom_TopFrontRightVert", "panelRight?panelRight_BottomBackLeftVert", "Point" )
#panelAssembly.constrain( "panelBottom?panelBottom_TopFace", "panelRight?panelRight_RightFace", "Axis" )

## Place panelBack
#panelAssembly.constrain( "panelBack?panelBack_BottomBackLeftVert", "panelBottom?panelBottom_TopBackLeftVert", "Point" )
#panelAssembly.constrain( "panelBack?panelBack_BottomBackRightVert", "panelBottom?panelBottom_TopBackRightVert", "Point" )
#panelAssembly.constrain( "panelBack?panelBack_TopBackLeftVert", "panelTop?panelTop_BottomBackLeftVert", "Point" )


## Solve panelAssembly
#panelAssembly.solve()