#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:47:50 2020

@author: neelu
"""

import numpy as np

def design_space(sigma_selected = 20):
    
    """
    This module will create the X matrix for selected number of singular values.
    
    Input:number of singular values to be selected
    Output:X_martix (new randomly created covariance matrix 
            for those number of singular values )
    """
    
    with open('../../../Project_Phase_fNRAND1/optimizer_input/design_range.csv') as f:
        f = np.loadtxt(f)
        A_limits = f[ : sigma_selected, : ]
        
    with open('../../../Project_Phase_fNRAND1/optimizer_input/matrix_vh.csv') as g:
        g = np.loadtxt(g)
        vh = g[ : sigma_selected, : ]
        
    A = []      #represent the matrix multiplication of new U matrix and diag(s) of SVD.
    for i in range(len(A_limits)):
        A.append(np.random.uniform(A_limits[i,0], A_limits[i,1],size=(sigma_selected))) #sigma random values created.
        
    A = np.transpose(A)
    X_matrix = np.matmul(A , vh)

    return(X_matrix ,sigma_selected)
    
