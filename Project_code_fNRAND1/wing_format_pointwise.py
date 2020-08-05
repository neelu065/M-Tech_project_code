#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:06:48 2020

@author: neelu
"""


def wing_format(g, wing):
    """
    This module will take the coordinates of wing as input and
    arrange those in *.p3d file format.
    """

    g.write('{0} \t\t {1} \t\t {2} \n'.format(200, 300, 1))  # You may need to change these value accordingly.

    for j in range(len(wing[0])):
        g.write('{} \t'.format(wing[0, j]))  # x_coordintes(chord_axis).
    g.write('\n')

    for j in range(len(wing[0])):
        g.write('{} \t'.format(wing[1, j]))  # y_coordintes(span_axis).
    g.write('\n')

    for j in range(len(wing[0])):
        g.write('{} \t'.format(wing[2, j]))  # z_coordintes(thickness_axis).
