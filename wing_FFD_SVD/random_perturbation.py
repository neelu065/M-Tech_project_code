#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:40:24 2020

@author: neelappagouda
"""
import numpy as np


def cp_new(iteration):
    """
    This module randomly create a new control points and written into a file.

    Input: Tolerance zone(radius) around each initial control points.
    Output: new control points written into a file.
    """

    with open('output_files/initial_cp.csv', 'r') as f:
        Cp_old = np.loadtxt(f).T  # Imp : Transpose

    with open('input_files/design_space.csv', 'r') as g:
        Radius = np.loadtxt(g).T  # Imp : Transpose

    # Cp_new_along chord begins...
    radius_x = Radius[0 , :]    # first row selected
    Cp_new_x = np.random.uniform(Cp_old[0, :] - radius_x, Cp_old[0, :] + radius_x)
    # Cp_new along chord ends...

    # Cp_new_along_span begins...
    radius_y = Radius[1, :]     # second row selected
    random_y = []
    
    ls = [0, 10, 20, 30, 40, 50]
    
     
    for i in ls:
        a = np.random.uniform(-radius_y[i] , radius_y[i])
        random_y.append(a)
    
    # Elements are repeated for several times
    perturbed_y = np.asarray([value for value in random_y for i in range(int(len(radius_y) / len(ls)))])
    Cp_new_y = Cp_old[1, :] + perturbed_y
   
    # Cp_new_along span ends...
    
    
    # Cp_new_along thickness begins...
    Cp_new_z = np.zeros(len(Cp_new_x))
    radius_z = Radius[2 , :]    # third row selected
    Cp_new_z[ls] = np.random.uniform(Cp_old[2 , ls] + radius_z[ls] , Cp_old[2, ls] - radius_z[ls] ) 
    
    for i in ls:
        for j in range(1 , 5):
            Cp_new_z[i + j] = np.random.uniform(Cp_new_z[i] + radius_z[i + j], Cp_new_z[i] - radius_z[i + j] )
        for j in range(5 , 10):
            Cp_new_z[i + j] = np.random.uniform(Cp_new_z[i + j - 5] , Cp_new_z[i + j - 5] + radius_z[i + j] )
    #Cp_new_along thickness ends...

    with open('output_files/perturbed_cp/cp_{}.csv'.format(iteration), 'w') as g:
        for i in range(len(Cp_new_x)):
            g.write("{} \t\t\t {} \t\t\t {}\n".format(Cp_new_x[i], Cp_new_y[i], Cp_new_z[i]))
