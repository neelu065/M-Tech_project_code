#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Feb 29 14:12:46 2020

@author: neelu
"""

import time

from make_dirs import make_directories
from template_copy import template_copy_replace
from design_final import restart_design_point
from check_slurm_file import check_slurm_out_file
from dependency_job_submit import dependency_job_submit
from read_history import read_cl_cd
from move_files import move_files
from mut_cross import mutation_crossover
from wing_iter_regenerator import wing_regenerator_iter
from generation_mesh_sol import gen_mesh_solution
from selection import selection
from remove_folder import remove_folder
from design_final import design_point


restart_from_gen = 1
final_generation = 5
singular_values_selected = 20  # work for all values </= 30
population_size = 4
mut = 0.9
cross_over_prob = 0.9
wait = "Yes"
deep_sleep = 10
short_sleep = 3

pw_path = '/scratch/neelappagouda/PointwiseV18.2R2'

path = 'optimizer_output'
perturbed_wing_file_path = 'optimizer_output/pointwise_template_files'
su2_template_file_path = 'optimizer_output/su2_config_files'
sbatch_destination = 'optimizer_output/sbatch_template_files'

print('Recreating the directories which are not existing {}...\n'.format(path))
make_directories(path)

print('copying the files into their destination ...\n')
template_copy_replace(population_size)  # copy and replace the strings within the f

dependency_job_submit(path, final_generation, init_gen=restart_from_gen + 1 )

target_vector = restart_design_point(path,restart_from_gen)

print('Storing the objective function values to the file...\n')
fobj_target, Cmx_target = read_cl_cd(population_size, restart='Yes')

for i in range(restart_from_gen, final_generation):            # parallel decomposition begins ...
    
    trial_vector = mutation_crossover(population_size, target_vector, cross_over_prob, singular_values_selected, mut)
    
    wing_regenerator_iter(trial_vector, singular_values_selected)
    
    results = gen_mesh_solution(trial_vector, population_size, pw_path, sbatch_destination, perturbed_wing_file_path, i+1, target_vector, cross_over_prob, mut, singular_values_selected)

    print('checking for slurm-*.out files\n')
    check_slurm_out_file(deep_sleep, short_sleep)
    
    trial_vector = [result for result in results]

    fobj_trial, Cmx_trial = read_cl_cd(population_size, i+1)
    
    fobj_target , target_vector, Cmx_target = selection( target_vector, trial_vector, fobj_trial, fobj_target, Cmx_target, Cmx_trial, path )
    
    move_files(path, i+1)

    design_point(path, target_vector, i + 1 )
    
    print('#### Generation_{} completed ... #### '.format(i + 1))

remove_folder(path)

print("####Optimization completed ... #####")
