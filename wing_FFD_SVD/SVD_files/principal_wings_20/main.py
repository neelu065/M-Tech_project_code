#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:02:20 2020

@author: neelu
"""
import numpy as np

from principal_wing_generator import wing_generator
from design_vectors_generator import design_space
from wing_format_pointwise import wing_format
from delete_files import delete_files
from make_dirs import make_directories

number_of_wings=1000 
number_of_sigma_selected=30

# Deleting folders
print('Deleting previous files ...\n')
delete_files()

# creating folders
print('Creating the directory...\n')
make_directories()

# wing_generator(number of wings, number of singular value selected)
x_standard , x_centered_vector = wing_generator(number_of_wings, number_of_sigma_selected)   

#design_space(number of singular value selected)
X_matrix ,sigma_selected = design_space(number_of_sigma_selected)

for i in range(sigma_selected):
    wing = x_standard + x_centered_vector + X_matrix[i]
     
    wing = np.reshape(wing,(int(len(wing.T)/3),3))
    
    wing = wing.T

    with open('random_wings/wing_perturbed_{}.x'.format(i+1),'w') as g:  #Perturbed wing formatting begins.
        wing_format(g,wing,i)                 # formating function 
    print('wing_perturbed_{} completed'.format(i+1))
