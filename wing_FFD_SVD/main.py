#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jan 13 09:34:07 2020

@author: neelappagouda
"""

from X_new import X_new
from delete_files import delete_files
from format_wing import format_wing
from interpolate import interpolate
from newfile import standard_wing
from parametric_coord import parameter
from random_perturbation import cp_new
import time

# Inputs to the python script
c_points_along_chord = 5
c_points_along_thickness = 2
c_points_along_span = 6

number_of_wing = 5
total_max_rms_wing_plot = number_of_wing

path = 'output_files'

print('Deleting previous files ...\n')
delete_files(path)

print('Interpolating the control points ...\n')
# function which interpolate the control point
delta_x, delta_y, delta_z, corner_point = interpolate(c_points_along_chord, c_points_along_thickness,
                                                      c_points_along_span)

print('Rewriting the given wing coordinate ...\n')
# rewrite the standard wing co_ord into output folder
standard_wing()

print('Converting the Cartesian space of Baseline wing into Parametric space ...\n')
# Cartesian space to Parametric space
parameter(delta_x, delta_y, delta_z, corner_point)

print('Creating {} different control point vectors using random function ...\n'.format(number_of_wing))
for i in range(number_of_wing):
    # new_cp = cp_new( tolerance for perturbation )
    cp_new(i + 1)  # new perturbed control points.

print('Creating {} different wing using random function ...\n'.format(number_of_wing))
for i in range(number_of_wing):
    # function return the new cartesian Coordinate of wing
    X_new(c_points_along_chord , c_points_along_span , c_points_along_thickness, i + 1)
    print('wing_{} created ...\n '.format(i + 1))

print('Rewriting the unformat_wing into standard format ... \n')
for i in range(number_of_wing):
    # function will rewrite the unformatted wing data to standard Plot3D format.
    format_wing(i + 1)
    print('pointwise_wing_{} created ...\n'.format(i + 1))


print("script end")
