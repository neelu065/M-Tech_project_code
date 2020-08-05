#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 08:40:40 2020

@author: neelappagouda
"""

import pandas as pd


def parameter(delta_x, delta_y, delta_z, point):
    """
    given a standard airfoil iin cartesian coordinate, it
    converts those values into parametric coordinate, and write it to
    parameter.csv.

    input: cartesian coordinate
    output: parametric coordinate
    """

    with open('output_files/initial_wing.csv', 'r') as fg:
        with open('output_files/parameter.csv', 'w') as f:
            df_airfoil = pd.DataFrame(fg)

            for row in range(len(df_airfoil)):
                value = df_airfoil.iat[row, 0].split()
                
                temp_x = float(value[0]) - float(point[0])      # Difference between
                s = temp_x / delta_x                            # given point and corner point

                temp_y = float(value[1]) - float(point[1])
                t = temp_y / delta_y
                
                temp_z = float(value[2]) - float(point[2])
                u = temp_z / delta_z

                f.write('{0} \t {1} \t {2} \n'.format( s, t, u ))

