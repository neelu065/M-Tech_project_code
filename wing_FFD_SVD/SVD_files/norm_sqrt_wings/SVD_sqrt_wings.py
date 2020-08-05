#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:52:58 2020

@author: neelu
"""

import numpy as np
import matplotlib.pyplot as plt

number_of_wings = 1000
number_of_sigma_selected = 150

x_standard = []
x_perturbed = []

with open('../../output_files/initial_wing.csv', 'r') as f:
    wing_standard = np.loadtxt(f)
    for j in range(len(wing_standard)):
        x_standard.append([wing_standard[j][0], wing_standard[j][1], wing_standard[j][2]])

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

X = x_error_matrix - x_centred_vector

print('Importing of all wings completed...')
print('performing SVD ...')

u, s, vh = np.linalg.svd(X, full_matrices=False)

total_energy = np.sum(s ** 2)

Norm = []
percentage_energy = []

for n in range(number_of_sigma_selected):
    fraction_energy = np.sum(s[:n+1] ** 2)

    percentage_space_covered = (fraction_energy / total_energy) * 100

    percentage_energy.append(percentage_space_covered)

    matrix_u_s = np.matmul(u[:, :n+1], np.diag(s[:n+1]))

    matrix_u_s_vh = np.matmul(matrix_u_s, vh[:n+1, :])

    Norm.append(np.linalg.norm(X - matrix_u_s_vh))

Norm_n = Norm/np.sqrt(number_of_wings)
with open('sigma_energy_norm_sqrt_n.csv', 'w') as f:
    for i in range(number_of_sigma_selected):
        f.write('{} \t\t {} \t\t {}\n'.format(i + 1, percentage_energy[i], Norm_n[i]))
# plt.figure(1)
# plt.grid(which='both')
# plt.plot(range(1 , number_of_sigma_selected+1 ), Norm, '*')
#
# plt.semilogy()
#
# plt.show()
#
# plt.figure(2)
# plt.grid(which='both')
# plt.plot(range(1 , number_of_sigma_selected+1 ), percentage_energy, '*')
# plt.show()
