#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:40:40 2020

@author: neelappagouda
"""

import numpy as np

def interpolate( m = 2 , n = 2 , p = 2):
    
    """
    This function interpolates the ffd box and return cp_coordinates, 
    which is further written to a file. 
    Also it return delta_x, delta_y and delta_z of the given ffd box.
        
    input: ffd corner points
    output: interpolated control points.
    """
    
    value = []
    
    with open('input_files/ffd.su2', 'r') as f:
        for line in f:
            if not '=' in line:
                value.append(line)
    
    point_1 = value[0].split(' ')         # point_1 =  [x0, y0, z0] 
    point_2 = value[6].split(' ')         # point_2 =  [x1, y1, z1] 
    
    x1 = np.float(point_1[0])
    y1 = np.float(point_1[1])
    z1 = np.float(point_1[2])

    x2 = np.float(point_2[0])
    y2 = np.float(point_2[1])
    z2 = np.float(point_2[2])

    
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_z = z2 - z1

    # Interploation function begins.
    x_inter = np.linspace(x1,x2,m)
    y_inter = np.linspace(y1,y2,p)
    z_inter = np.linspace(z1,z2,n)
    
    with open('output_files/initial_cp.csv', 'w') as f:
        for j in y_inter:
            for k in z_inter:
                for i in x_inter:
                    f.write('{} \t\t\t {} \t\t\t {} \n'.format( i, j, k ))
    
    return delta_x, delta_y, delta_z, point_1
