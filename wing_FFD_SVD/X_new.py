#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:33:15 2020

@author: neelappagouda
"""
import numpy as np
import math


def X_new(a, b, c, iteration):
    """
    For the perturbed control points,
    new deformed airfoil cartesian coordinates are obtained.

    input: number of control points in each direction.
    output: deformed airfoil written into a file.
    """

    with open('output_files/perturbed_cp/cp_{}.csv'.format(iteration), 'r') as f:
        with open('output_files/parameter.csv', 'r') as g:
            with open('output_files/perturbed_wing/unformat_wing/wing_{}.csv'.format(iteration), 'w') as X_new:

                cp_new = np.loadtxt(f)
                parameter = np.loadtxt(g)

                n = a - 1
                m = b - 1
                p = c - 1
                for k in range(len(parameter)):
                    s = parameter[k, 0]
                    t = parameter[k, 1]
                    u = parameter[k, 2]

                    z = 0
                    temp = 0

                    # FFD Box equation.
                    for j in range(b):
                        for q in range(c):
                            for i in range(a):
                                # Finding binomial coeffiecient.
                                bi_coeff_S = math.factorial(n) / (math.factorial(n - i) * math.factorial(i))
                                bi_coeff_T = math.factorial(m) / (math.factorial(m - j) * math.factorial(j))
                                bi_coeff_U = math.factorial(p) / (math.factorial(p - q) * math.factorial(q))

                                S = (bi_coeff_S) * (s ** i) * ((1 - s) ** (n - i))
                                T = (bi_coeff_T) * (t ** j) * ((1 - t) ** (m - j))
                                U = (bi_coeff_U) * (u ** q) * ((1 - u) ** (p - q))

                                temp += S * T * U * cp_new[z]
                                z += 1

                    X_new.write('{} \t {} \t {} \n'.format(temp[0], temp[1], temp[2]))
