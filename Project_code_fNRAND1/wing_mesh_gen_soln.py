#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:10:50 2020

@author: neelu
"""

import os
import concurrent.futures

from create_wing import create_wing
from sbatch_file import sbatch_file


def create_wing_mesh_soln(population_size, pointwise_path, perturbed_wing_file_path, sbatch_destination,
                          singular_values_selected):
    
    """
    This module will create the wing , mesh over it,
    and find the CFD solution to it.

    Input: respective paths
    Output: Cl , Cd, target
    """
    
    sbatch_file(population_size, gen = 0)
    
    def gen_meshing_sol(i):
        
        """
        This module will create the mesh files (*.su2) using pointwise.
        And is place in while loop with the intention to eliminate the 
        wrinkled wing surfaces.
        """
        
        while not os.path.isfile('optimizer_output/mesh_files/wing_{}.su2'.format(i)):
            
            print('generating the wing_{}, followed by meshing and finding solution ...\n'.format(i))
    
            target = create_wing(singular_values_selected, 1, i)
    
            command = '{}/pointwise -b {}/pointwise_template_{}.glf'.format(pointwise_path, perturbed_wing_file_path, i)
            os.system(command)
    
        print('wing_{}.su2 file created ...'.format(i))

        return target

    with concurrent.futures.ThreadPoolExecutor() as executor:
        iterator = range(1,population_size+1)
        results = executor.map(gen_meshing_sol,
                               iterator)  # map func will output the results (value) in the same sequence.

    return results
