#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:54:23 2020

@author: neelappagouda
"""

import numpy as np

def format_wing(iteration):

    """
    This module is called when the perturbed unformatted wing is created.
    This raw data of wing is converted back into standard Plot3D file format.

    input: Raw data of wing.
    output: Standard Plot3D file format of wing.
    """

    with open('output_files/perturbed_wing/unformat_wing/wing_{}.csv'.format(iteration),'r') as f:
        a = np.loadtxt(f)
        b = np.transpose(a)

        c_1 = np.reshape(b[0],(int(len(a)/4),4))
        c_2 = np.reshape(b[1],(int(len(a)/4),4))
        c_3 = np.reshape(b[2],(int(len(a)/4),4))

    with open('output_files/perturbed_wing/format_wing/pointwise_wing_{}.x'.format(iteration),'w') as g:
        g.write('{0} \t\t {1} \t\t {2} \n'.format(300,100,1))

        # Below line are highly sensitive, better not to alter them.
        for i in range(len(c_1)):
            for k in range(len(c_1[0,:])):
                g.write('{} \t\t'.format(c_1[i][k]))
            g.write('\n')

        for i in range(len(c_2)):
            for k in range(len(c_2[0,:])):
                g.write('{} \t\t'.format(c_2[i][k]))
            g.write('\n')

        for i in range(len(c_3)):
            for k in range(len(c_3[0,:])):
                g.write('{} \t\t'.format(c_3[i][k]))
            g.write('\n')


