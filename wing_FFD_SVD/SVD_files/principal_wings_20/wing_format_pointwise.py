#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:06:48 2020

@author: neelu
"""
def wing_format(g,wing,i):
    
    g.write('{0} \t\t {1} \t\t {2} \n'.format(300,100,1))   #You may need to change these value accordingly.
    for j in range(len(wing[0])):           
        g.write('{} \t'.format(wing[0,j]))      # x_coordintes.
    g.write('\n')
    
    for j in range(len(wing[0])):
        g.write('{} \t'.format(wing[1,j]))      # y_coordintes.
    g.write('\n')
    
    for j in range(len(wing[0])):
        g.write('{} \t'.format(wing[2,j]))      # z_coordintes.
    