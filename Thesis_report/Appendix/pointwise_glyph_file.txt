package require PWI_Glyph 2.18.2

pw::Application reset
pw::Application markUndoLevel {Journal Reset}
pw::Application clearModified


set myScriptName [info script]
set myScriptFolder [file dirname $myScriptName]
set myFullyQualifiedName [append myScriptFolder "/../wing_pointwise/wing_0.x"]
#puts [format "File Name             %s" $myFullyQualifiedName]

set meshLocation [file dirname $myScriptName]
set meshFileLoaction [append meshLocation "/../mesh_files/wing_0.su2"]
#puts [format "Reading data file              %s" $meshFileLoaction]

set _TMP(mode_1) [pw::Application begin GridImport]
  $_TMP(mode_1) initialize -strict -type PLOT3D $myFullyQualifiedName
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Grid}


set con(1) [pw::GridEntity getByName con-2]
set myConnectorDimension [$con(1) getDimension]

#setting the first value as minimum point.
set min_x [lindex [$con(1) getXYZ 1]  0]

# If True than replace value of min_x with new value.
for { set a 1}  {$a <= $myConnectorDimension} {incr a} {
	set temp_x [lindex [$con(1) getXYZ $a]  0]
	if {$temp_x < $min_x} {
		set min_x $temp_x
		set ind $a
	}
}

# variable "ind" will contain index number for minimum x_coordinate point.
set pt_min_x [lindex [$con(1) getXYZ $ind]  0]
set pt_min_y [lindex [$con(1) getXYZ $ind]  1]
set pt_min_z [lindex [$con(1) getXYZ $ind]  2]


list myMinXYZ ""
lappend myMinXYZ $pt_min_x
lappend myMinXYZ $pt_min_y
lappend myMinXYZ $pt_min_z
set newSplitParams [list]
lappend newSplitParams [$con(1) getParameter -closest [pw::Application getXYZ [$con(1) closestPoint $myMinXYZ ]]]
set myListOfConsAfterSplit [$con(1) split $newSplitParams]
unset myListOfConsAfterSplit
unset newSplitParams

##################################### Creating Wingtip  ############################################


set _TMP(mode_1) [pw::Application begin Create]
set _TMP(PW_1) [pw::SegmentConic create]
set _CN(3) [pw::GridEntity getByName con-2-split-2]
set _CN(1) [pw::GridEntity getByName con-2-split-1]

## Find end of connector closest to the first point picked
    set pt1 [$_CN(3) getXYZ -arc 0.0]
    set pt2 [$_CN(3) getXYZ -arc 1.0]
    set pt1_x [lindex $pt1  0]
    set pt1_y [lindex $pt1  1]
    #set pt1_z [lindex $pt1  2]
    set pt2_x [lindex $pt2  0]
    set pt2_y [lindex $pt2  1]
    #set pt2_z [lindex $pt2  2]

##################(% of span) Span connector(con_span) is used to create proper wing_tip #############
set con_span [pw::GridEntity getByName con-1]

set tip_percentage 0.02
set temp_tip_diff [lindex [$con_span getXYZ -arc 1.0] 1]
set tip_diff [expr ($temp_tip_diff * $tip_percentage)]

set dim_span [$con_span getDimension]

set temp_1_y [lindex [$con_span getXYZ [expr (($dim_span - 1))]]  1]
set temp_1_z [lindex [$con_span getXYZ [expr (($dim_span - 1))]]  2]

set temp_2_y [lindex [$con_span getXYZ $dim_span]  1]
set temp_2_z [lindex [$con_span getXYZ $dim_span]  2]

set temp_var [ expr (( - $tip_diff) * (($temp_1_z - $temp_2_z)/($temp_1_y - $temp_2_y)))]

    ## Calculate X, Y, Z for the conic
    set conicX [ expr ( ($pt1_x * 0.75 + $pt2_x * 0.25) ) ]
    set conicZ [ expr ( ($temp_2_z - $temp_var ) ) ]
    set conicY [ expr ( ($pt1_y + $tip_diff ) ) ]
    
    set pt3 [ format "%s %s %s" $conicX $conicY $conicZ]

    ## create the conic
          set thisCreateMode [pw::Application begin Create]
	  set thisTmpEntity [pw::SegmentConic create]
	  $thisTmpEntity addPoint $pt1
	  $thisTmpEntity addPoint $pt2
	  $thisTmpEntity setShoulderPoint $pt3
	  set _CN(5) [pw::Connector create]
	  $_CN(5) addSegment $thisTmpEntity
	  $_CN(5) calculateDimension
	  unset thisTmpEntity
	$thisCreateMode end
	unset thisCreateMode

unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)

set di [$_CN(1) getDimension]

$_CN(5) setDimension $di
pw::CutPlane refresh
pw::Application markUndoLevel {Dimension}

pw::Application setGridPreference Unstructured
set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(5) $_CN(3)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(5) $_CN(1)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}
puts [ format " Wingtip created ...  "  ]


##################################### Wingtip created successful  ##################################



set _DM(1) [pw::GridEntity getByName dom-3]
set _DM(2) [pw::GridEntity getByName dom-2]
set _DM(3) [pw::GridEntity getByName dom-1]
set _TMP(mode_1) [pw::Application begin Modify [list $_DM(3) $_DM(2) $_DM(1)]]
  set _TMP(PW_1) [pw::GridShape create]
  set _TMP(PW_2) [pw::TRexCondition create]
  $_TMP(PW_2) setConditionType Match
  $_TMP(PW_2) setName BuildBlocksMatch
  $_TMP(PW_2) setAdaptation On
  unset _TMP(PW_2)
  set _TMP(PW_2) [pw::TRexCondition create]
  $_TMP(PW_2) setConditionType Off
  $_TMP(PW_2) setName BuildBlocksOff
  $_TMP(PW_2) setAdaptation On
  unset _TMP(PW_2)
  $_TMP(PW_1) box -width 30.6943930844 -height 35.9467829743 -length 31.5240822916
  $_TMP(PW_1) setGridType Unstructured
  $_TMP(PW_1) setTransform [list 0 0 -1 0 0 1 0 0 1 -0 0 0 -15.3316275849 -2.48689957516e-14 0.186542155619 1]
  $_TMP(PW_1) setSectionQuadrants 2
  $_TMP(PW_1) setIncludeEnclosingEntitiesInBlock 1
  $_TMP(PW_1) setGridBoundary FromSizeField
  $_TMP(PW_1) setSizeFieldDecay [pw::GridEntity getDefault SizeFieldDecay]
  $_TMP(PW_1) setSizeFieldBackgroundSpacing [pw::GridEntity getDefault SizeFieldBackgroundSpacing]
  $_TMP(PW_1) setEnclosingEntities [list $_DM(1) $_DM(2) $_DM(3)]
  $_TMP(PW_1) clearSizeFieldEntities
  $_TMP(PW_1) includeSizeFieldEntity [list $_DM(1) $_DM(2) $_DM(3)] true
  $_TMP(PW_1) updateGridEntities -updateBlockAttributes
  set _TMP(blocks) [$_TMP(PW_1) getGridEntities -type pw::Block]
  set _TMP(blockCollection) [pw::Collection create]
  $_TMP(blockCollection) set $_TMP(blocks)

  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexMaximumLayers 0
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexFullLayers 0
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexGrowthRate 1.2
  set _TMP(bc) [pw::TRexCondition getByName BuildBlocksMatch]
  set _TMP(doms) [$_TMP(PW_1) getBlockRegisters Symmetry]
  $_TMP(bc) apply $_TMP(doms)

  unset _TMP(bc)
  unset _TMP(doms)
  set _TMP(bc) [pw::TRexCondition getByName BuildBlocksOff]
  set _TMP(doms) [$_TMP(PW_1) getBlockRegisters Other]
  $_TMP(bc) apply $_TMP(doms)

  unset _TMP(bc)
  unset _TMP(doms)
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexPushAttributes 1
  $_TMP(blockCollection) do pushAttributes
  $_TMP(blockCollection) do boundaryAdaptation
  $_TMP(blockCollection) delete
  unset _TMP(blocks)
  unset _TMP(blockCollection)
  set _BL(1) [pw::GridEntity getByName blk-1]
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Build Blocks}


set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_BL(1)]]
  set _TMP(PW_1) [pw::TRexCondition getByName Unspecified]
  set _TMP(PW_2) [pw::TRexCondition getByName BuildBlocksMatch]
  set _TMP(PW_3) [pw::TRexCondition getByName BuildBlocksOff]
  set _DM(4) [pw::GridEntity getByName dom-9]
  set _DM(5) [pw::GridEntity getByName dom-4]
  set _DM(6) [pw::GridEntity getByName dom-5]
  set _DM(7) [pw::GridEntity getByName dom-6]
  set _DM(8) [pw::GridEntity getByName dom-7]
  set _DM(9) [pw::GridEntity getByName dom-8]
  $_TMP(PW_2) setConditionType AdjacentGrid
  $_TMP(PW_3) setConditionType AdjacentGrid
  set _TMP(PW_4) [pw::TRexCondition create]
  set _TMP(PW_5) [pw::TRexCondition getByName bc-4]
  unset _TMP(PW_4)
  $_TMP(PW_5) setName WALL
  $_TMP(PW_5) apply [list [list $_BL(1) $_DM(3) Same] [list $_BL(1) $_DM(1) Opposite] [list $_BL(1) $_DM(2) Opposite]]
	$_TMP(PW_5) setConditionType Match
  $_TMP(PW_3) setAdaptation Off
  $_TMP(PW_2) setAdaptation Off
  $_TMP(mode_1) setStopWhenFullLayersNotMet true
  $_TMP(mode_1) setAllowIncomplete true
  $_TMP(mode_1) run Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

unset _TMP(PW_1)
unset _TMP(PW_2)
unset _TMP(PW_3)
unset _TMP(PW_5)


pw::Application setCAESolver SU2 3
pw::Application markUndoLevel {Select Solver}

pw::Application setCAESolver SU2 3
pw::Application markUndoLevel {Set Dimension 3D}

set _DM(1) [pw::GridEntity getByName dom-1]
set _BL(1) [pw::GridEntity getByName blk-1]
set _DM(2) [pw::GridEntity getByName dom-2]
set _DM(3) [pw::GridEntity getByName dom-3]
set _DM(4) [pw::GridEntity getByName dom-4]
set _DM(5) [pw::GridEntity getByName dom-5]
set _DM(6) [pw::GridEntity getByName dom-6]
set _DM(7) [pw::GridEntity getByName dom-7]
set _DM(8) [pw::GridEntity getByName dom-8]
set _DM(9) [pw::GridEntity getByName dom-9]
set _TMP(PW_1) [pw::BoundaryCondition getByName Unspecified]
set _TMP(PW_2) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_3) [pw::BoundaryCondition getByName bc-2]
unset _TMP(PW_2)
$_TMP(PW_3) setName XNORMAL_FACES
pw::Application markUndoLevel {Name BC}

set _TMP(PW_4) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_5) [pw::BoundaryCondition getByName bc-3]
unset _TMP(PW_4)
$_TMP(PW_5) setName YNORMAL_FACE
pw::Application markUndoLevel {Name BC}

set _TMP(PW_6) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_7) [pw::BoundaryCondition getByName bc-4]
unset _TMP(PW_6)
$_TMP(PW_7) setName ZNORMAL_FACES
pw::Application markUndoLevel {Name BC}

set _TMP(PW_8) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_9) [pw::BoundaryCondition getByName bc-5]
unset _TMP(PW_8)
$_TMP(PW_9) setName WALL
pw::Application markUndoLevel {Name BC}

set _TMP(PW_10) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_11) [pw::BoundaryCondition getByName bc-6]
unset _TMP(PW_10)
$_TMP(PW_11) setName SYMMETRY
pw::Application markUndoLevel {Name BC}

$_TMP(PW_3) apply [list [list $_BL(1) $_DM(5)] [list $_BL(1) $_DM(4)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_11) apply [list [list $_BL(1) $_DM(9)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(6)] [list $_BL(1) $_DM(8)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_5) apply [list [list $_BL(1) $_DM(7)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_9) apply [list [list $_BL(1) $_DM(2)] [list $_BL(1) $_DM(3)] [list $_BL(1) $_DM(1)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_1)
unset _TMP(PW_3)
unset _TMP(PW_5)
unset _TMP(PW_7)
unset _TMP(PW_9)
unset _TMP(PW_11)

set _TMP(mode_1) [pw::Application begin CaeExport]
  $_TMP(mode_1) addAllEntities
  $_TMP(mode_1) initialize -strict -type CAE $meshFileLoaction
  $_TMP(mode_1) setAttribute FilePrecision Double
  $_TMP(mode_1) verify
  $_TMP(mode_1) write
$_TMP(mode_1) end
unset _TMP(mode_1)

