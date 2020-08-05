#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:52:58 2020

@author: neelu
"""

import numpy as np
from wing_format_pointwise import wing_format
np.set_printoptions(threshold=np.inf)

def wing_generator(number_of_wings=1000 , number_of_sigma_selected=30):
    """
    This module will take randomly created 1000 wings and 
    calculate SVD of the their coriance matrix.
    Further it even plots the principal component vector wings.
    
    Return: x_standard (naca0012 wing coordinates), 
            x_centered_vector (average of all errors in perturbed wings)
            
    Input : 1000 wings x, y, z coordinates.
    Output: file containing design_space (max,min) values for all variables, 
            matrix_vh file containing 30 principal vectors, 
            and the pointwise file for those principal vectors wings.  
    """

    x_standard = []
    x_perturbed = []

    with open('../../output_files/initial_wing.csv', 'r') as f:
        wing_standard = np.loadtxt(f)
        for j in range(len(wing_standard)):
            x_standard.append([wing_standard[j][0], wing_standard[j][1], wing_standard[j][2]])

    with open('../../../Project_Phase_fNRAND1/optimizer_input/initial_baseline_wing.csv', 'w') as f:
        for i in range(len(x_standard)):
            for j in range(len(x_standard[0])):
                f.write('{}\t\t'.format(x_standard[i][j]))

    for i in range(number_of_wings):
        with open('../../output_files/perturbed_wing/unformat_wing/wing_{}.csv'.format(i + 1), 'r') as f_read:
            wing_perturbed = np.loadtxt(f_read)
            for j in range(len(wing_perturbed)):
                x_perturbed.append([wing_perturbed[j][0], wing_perturbed[j][1], wing_perturbed[j][2]])
            print('wing_{} completed'.format(i))

    wing_perturbed_matrix = np.reshape(x_perturbed, (number_of_wings, len(x_standard) * 3))

    x_standard = np.reshape(x_standard, (1, len(x_standard) * 3))

    x_error_matrix = wing_perturbed_matrix - x_standard

    x_centred_vector = x_error_matrix.mean(axis=0)  # along columns

    with open('../../../Project_Phase_fNRAND1/optimizer_input/x_centered_error_vector.csv', 'w') as f:
        for i in range(len(x_centred_vector)):
            f.write('{}\t\t'.format(x_centred_vector[i]))

    X = x_error_matrix - x_centred_vector

    print('Importing of all wings completed...')

    print('performing SVD ...')

    u, s, vh = np.linalg.svd(X, full_matrices=False)

    matrix_u_s = np.matmul(u[:, :number_of_sigma_selected], np.diag(s[:number_of_sigma_selected]))

    matrix_vh = vh[:number_of_sigma_selected , :]

    matrix_u_s_vh = np.matmul(matrix_u_s, matrix_vh)

    alp_max = np.ndarray.max(matrix_u_s,axis=0)      # Calculate the max along columns.
    alp_min = np.ndarray.min(matrix_u_s,axis=0)     # Calculate the min along columns.

    d_space = np.where( abs(alp_max) < abs(alp_min), abs(alp_max), abs(alp_min) )     # Important step since values were not symmetry.

    with open('../../../Project_Phase_fNRAND1/optimizer_input/design_range.csv', 'w') as f:
        for i in range(number_of_sigma_selected):
            f.write('{0} \t\t {1} \n'.format(-d_space[i],d_space[i]))
            #f.write('{0} \t\t {1} \n'.format(alp_min[i],alp_max[i]))

    with open('../../../Project_Phase_fNRAND1/optimizer_input/matrix_vh.csv', 'w') as f:
        for i in range(len(matrix_vh)):
            for j in range(len(matrix_vh.T)):
                f.write('{} \t'.format(matrix_vh[i][j]))
            f.write('\n')

    for i in range(number_of_sigma_selected):
        wing = x_standard + x_centred_vector + matrix_u_s_vh[i]
        wing = np.reshape(wing,(int(len(wing.T)/3),3))      #Transpose of wing matrix is important.
        wing = wing.T

        with open('principal_wings/principal_wing_{}.x'.format(i+1),'w') as g:  #Principal wing formatting begins.
            wing_format(g,wing,i)                 # formating function
        print('principal_wing_{} completed'.format(i+1))

    return (x_standard , x_centred_vector)

