#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:05:27 2020

@author: neelappagouda
"""

import os


def make_directories(path):
    
    """
       As the name suggests this module will create
       the folders at respective positions.
    """
    if not os.path.exists('{}'.format(path)):
        os.mkdir('{}'.format(path))

    if not os.path.exists('{}/wing_pointwise'.format(path)):
        os.mkdir('{}/wing_pointwise'.format(path))
        os.mkdir('{}/mesh_files'.format(path))
        os.mkdir('{}/pointwise_template_files'.format(path))
        os.mkdir('{}/su2_config_files'.format(path))
        os.mkdir('{}/sbatch_template_files'.format(path))
        os.mkdir('{}/restart_naca_files'.format(path))
        os.mkdir('{}/sbatch_dependency_files'.format(path))

        os.mkdir('{}/su2_solution_files'.format(path))
        os.mkdir('{}/su2_solution_files/history_files'.format(path))
        os.mkdir('{}/su2_solution_files/restart_files'.format(path))
    else:
        os.system('rm -f {}/mesh_files/*'.format(path))

    if not os.path.exists('{}/solution_final'.format(path)):
        os.mkdir('{}/solution_final'.format(path))
        os.mkdir('{}/solution_final/volume_flow'.format(path))
        os.mkdir('{}/solution_final/surface_flow'.format(path))
        os.mkdir('{}/solution_final/design_vector'.format(path))

        os.mkdir('{}/generation_sol_files'.format(path))
        os.mkdir('{}/generation_sol_files/obj_func'.format(path))
