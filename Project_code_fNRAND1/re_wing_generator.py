#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:01:17 2020

@author: neelu
"""

import numpy as np
from wing_format_pointwise import wing_format


def re_wing_generator(X_matrix, i):
    
    """
    This module add the Co_variance matrix to the 
    standard baseline wing and the centered error vector.
    
    Input: Covariance matrix and index 
    Output: Perturbed wings associated with Principal vectors.
    """
    
    with open('optimizer_input/initial_baseline_wing.csv') as f:
        x_baseline = np.loadtxt(f)
    
    with open('optimizer_input/x_centered_error_vector.csv') as f:
        x_centered_error = np.loadtxt(f)
    
    wing = x_baseline + x_centered_error + X_matrix
         
    wing = np.reshape(wing,(int(len(wing.T)/3),3))
        
    wing = wing.T
    
    with open('optimizer_output/wing_pointwise/wing_{}.x'.format(i),'w') as g:  #Perturbed wing formatting begins.
        wing_format(g, wing)                 # formating function
    print('wing_{} recreated ...'.format(i))