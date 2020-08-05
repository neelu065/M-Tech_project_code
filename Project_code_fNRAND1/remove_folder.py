#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:58:03 2020

@author: neelu
"""
import os
from delete_slurm_files import delete_slurm_out_files


def remove_folder(path):
    os.system('rm -rf {}/wing_pointwise'.format(path))
    os.system('rm -rf {}/mesh_files'.format(path))
    os.system('rm -rf {}/pointwise_template_files'.format(path))
    os.system('rm -rf {}/su2_config_files'.format(path))
    os.system('rm -rf {}/sbatch_template_files'.format(path))
    os.system('rm -rf {}/restart_naca_files'.format(path))
    os.system('rm -rf {}/su2_solution_files'.format(path))
    os.system('rm -rf {}/sbatch_dependency_files'.format(path))

