package require PWI_Glyph 2.18.2

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}
pw::Application clearModified


set _TMP(mode_1) [pw::Application begin GridImport]
  $_TMP(mode_1) initialize -strict -type {PLOT3D} {/home/neelu/Desktop/Template_glyph/glyph_test/pointwise_wing_4.x}
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Grid}


set _DM(1) [pw::GridEntity getByName dom-1]
set _CN(1) [pw::GridEntity getByName con-1]

set _CN(2) [pw::GridEntity getByName con-3]
set _TMP(split_params) [list]
lappend _TMP(split_params) [lindex [list 101 1 $_DM(1)] 0]
lappend _TMP(split_params) [lindex [list 101 100 $_DM(1)] 0]
set _TMP(PW_1) [$_DM(1) split -I $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel {Split}


puts [ format " Wing successfully imported ...  "  ]
##################################### Creating Wingtip  ############################################



set _TMP(mode_1) [pw::Application begin Create]
set _TMP(PW_1) [pw::SegmentConic create]
set _CN(3) [pw::GridEntity getByName con-3-split-2]
set _CN(1) [pw::GridEntity getByName con-3-split-1]   

## Find end of connector closest to the first point picked
    set pt1 [$_CN(3) getXYZ -arc 0.0]
    set pt2 [$_CN(3) getXYZ -arc 1.0]
    set pt1_x [lindex $pt1  0]
    set pt1_y [lindex $pt1  1]
    set pt1_z [lindex $pt1  2]
    set pt2_x [lindex $pt2  0]
    set pt2_y [lindex $pt2  1]
    set pt2_z [lindex $pt2  2]
    
  
    puts [ format "    End Point 1: (%16.12s %16.12s %16.12s)" $pt1_x $pt1_y $pt1_z ]
    puts [ format "    End Point 2: (%16.12s %16.12s %16.12s)" $pt2_x $pt2_y $pt2_z ]
    
    ## Calculate X, Y, Z for the conic
    set conicX [ expr ( ($pt1_x * 0.75 + $pt2_x * 0.25) ) ]
    set conicZ [ expr ( ($pt1_z + $pt2_z)/2.0 ) ]
    set conicY [ expr ( ($pt1_y + 0.06 ) ) ]
    
    puts [ format "Calculated values for shoulder: " ] 
    puts [ format "                 (%16.12s %16.12s %16.12s)" $conicX $conicY $conicZ ]
    
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

$_CN(5) setDimension 101
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
puts [ format " Wingtip created successfully ...  "  ]



################################### VOLUME MESHING BEGIN ########################################




puts [ format " Performing T-Rex ...  "  ]
set _DM(1) [pw::GridEntity getByName dom-1-split-1]
set _DM(2) [pw::GridEntity getByName dom-1-split-2]
set _DM(3) [pw::GridEntity getByName dom-1]
set _DM(4) [pw::GridEntity getByName dom-2]


set _TMP(mode_1) [pw::Application begin Modify [list $_DM(1) $_DM(2) $_DM(3) $_DM(4)]]
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
  $_TMP(PW_1) box -width 30.1696433225 -height 36.1300965654 -length 31.0005501477
  $_TMP(PW_1) setGridType Unstructured
  $_TMP(PW_1) setTransform [list 0 0 -1 0 0 1 0 0 1 -0 0 0 -15.0005501477 -9.0361002389e-05 0.00196598531036 1]
  $_TMP(PW_1) setSectionQuadrants 2
  $_TMP(PW_1) setIncludeEnclosingEntitiesInBlock 1
  $_TMP(PW_1) setGridBoundary FromSizeField
  $_TMP(PW_1) setSizeFieldDecay [pw::GridEntity getDefault SizeFieldDecay]
  $_TMP(PW_1) setSizeFieldBackgroundSpacing [pw::GridEntity getDefault SizeFieldBackgroundSpacing]
  $_TMP(PW_1) setEnclosingEntities [list $_DM(4) $_DM(3) $_DM(2) $_DM(1)]
  $_TMP(PW_1) clearSizeFieldEntities
  $_TMP(PW_1) includeSizeFieldEntity [list $_DM(4) $_DM(3) $_DM(2) $_DM(1)] true
  $_TMP(PW_1) updateGridEntities -updateBlockAttributes

set _TMP(blocks) [$_TMP(PW_1) getGridEntities -type pw::Block]
set _TMP(blockCollection) [pw::Collection create]
$_TMP(blockCollection) set $_TMP(blocks)
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexPushAttributes 1
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexMaximumLayers 2
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexFullLayers 1
  $_TMP(blockCollection) do setUnstructuredSolverAttribute TRexGrowthRate 1.3
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
  set _TMP(PW_1) [pw::TRexCondition getByName {Unspecified}]
  set _TMP(PW_2) [pw::TRexCondition getByName {BuildBlocksMatch}]
  set _TMP(PW_3) [pw::TRexCondition getByName {BuildBlocksOff}]
  set _DM(5) [pw::GridEntity getByName dom-4]
  set _DM(6) [pw::GridEntity getByName dom-3]
  set _DM(7) [pw::GridEntity getByName dom-8]
  set _DM(8) [pw::GridEntity getByName dom-5]
  set _DM(9) [pw::GridEntity getByName dom-6]
  set _DM(10) [pw::GridEntity getByName dom-7]
  set _TMP(PW_4) [pw::TRexCondition create]
  set _TMP(PW_5) [pw::TRexCondition getByName {bc-4}]
  unset _TMP(PW_4)
  
  #$_TMP(PW_5) setName {EULER_WAL}
  #$_TMP(PW_5) setConditionType {Wall}
  #$_TMP(PW_5) apply [list [list $_BL(1) $_DM(3) Same] [list $_BL(1) $_DM(4) Same] [list $_BL(1)    
#$_DM(2) Opposite] [list $_BL(1) $_DM(1) Opposite]]
#  $_TMP(PW_2) setName {SYMMETRY_FACE}
#  $_TMP(PW_3) setConditionType {AdjacentGrid}
#  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(7) Same]]
#  $_TMP(mode_1) setStopWhenFullLayersNotMet true
  $_TMP(mode_1) setAllowIncomplete true
  $_TMP(mode_1) run Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Solve}

unset _TMP(PW_1)
unset _TMP(PW_2)
unset _TMP(PW_3)
unset _TMP(PW_5)
pw::Application setCAESolver {SU2} 3
pw::Application markUndoLevel {Select Solver}

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
$_TMP(PW_9) setName SYMMETRY
pw::Application markUndoLevel {Name BC}

set _TMP(PW_10) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_11) [pw::BoundaryCondition getByName bc-6]
unset _TMP(PW_10)
$_TMP(PW_11) setName UPPER_SIDE
pw::Application markUndoLevel {Name BC}

set _TMP(PW_12) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_13) [pw::BoundaryCondition getByName bc-7]
unset _TMP(PW_12)
$_TMP(PW_13) setName LOWER_SIDE
pw::Application markUndoLevel {Name BC}

set _TMP(PW_14) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_15) [pw::BoundaryCondition getByName bc-8]
unset _TMP(PW_14)
$_TMP(PW_15) setName TIP
pw::Application markUndoLevel {Name BC}

$_TMP(PW_3) apply [list [list $_BL(1) $_DM(5)] [list $_BL(1) $_DM(6)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(8)] [list $_BL(1) $_DM(10)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_5) apply [list [list $_BL(1) $_DM(9)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_11) apply [list [list $_BL(1) $_DM(1)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_13) apply [list [list $_BL(1) $_DM(2)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_15) apply [list [list $_BL(1) $_DM(3)] [list $_BL(1) $_DM(4)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_9) apply [list [list $_BL(1) $_DM(7)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_1)
unset _TMP(PW_3)
unset _TMP(PW_5)
unset _TMP(PW_7)
unset _TMP(PW_9)
unset _TMP(PW_11)
unset _TMP(PW_13)
unset _TMP(PW_15)
set _TMP(mode_1) [pw::Application begin CaeExport [pw::Entity sort [list $_BL(1)]]]
  $_TMP(mode_1) initialize -strict -type CAE {/home/neelu/Desktop/Template_glyph/wing_3.su2}
  $_TMP(mode_1) setAttribute FilePrecision Double
  $_TMP(mode_1) verify
  $_TMP(mode_1) write
$_TMP(mode_1) end
unset _TMP(mode_1)

puts [ format "Mesh file successfully generated ...  "  ]




