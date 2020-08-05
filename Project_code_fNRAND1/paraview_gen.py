#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:10:06 2020

@author: neelappagouda
"""

import os
import fileinput
import concurrent.futures
pop_size = 20

input_path = 'optimizer_input'
output_path = 'optimizer_output'

def main_sol(i):
    
    os.system('cp {}/paraview_template.cfg {}/solution_final/su2_config_{}.cfg'.format(input_path,output_path, i+1))
    
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("wing_0", "wing_{}".format(i + 1)).rstrip())
    
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("paraview_history_0", "paraview_history_{}".format(i + 1)).rstrip())
    
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("restart_flow_0", "restart_flow_{}".format(i + 1)).rstrip())
    
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("paraview_out_restart_0", "paraview_out_restart_{}".format(i + 1)).rstrip())
        
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("volume_flow_0", "volume_flow_{}".format(i + 1)).rstrip())
    
    for line in fileinput.input('{}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1), inplace=1):
        print(line.replace("surface_flow_0", "surface_flow_{}".format(i + 1)).rstrip())
        
    os.system('/scratch/neelappagouda/SU2_V-7.0/bin/SU2_CFD {}/solution_final/su2_config_{}.cfg'.format(output_path, i + 1))

with concurrent.futures.ProcessPoolExecutor() as executor:
    i = range(pop_size)
    executor.map(main_sol, i)
    
os.system('rm -f {}/solution_final/*.cfg'.format(output_path))
os.system('rm -f {}/solution_final/*.csv'.format(output_path))
os.system('rm -f {}/solution_final/*.dat'.format(output_path))
    
