#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:54:36 2020

@author: neelu
"""

import fileinput
import os


def sbatch_file(pop_size, gen = 0):
    
    """
    This module will replace few lines in sbatch_template_files (*.sh).
    Along with this it as make sure that different job name appear in sqeue.
    
    """
    
    sbatch_source = 'optimizer_input/sbatch_template.sh'
    sbatch_destination = 'optimizer_output/sbatch_template_files'
    
    for pop in range(pop_size):
        
        os.system('cp {0} {1}/sbatch_template_{2}.sh'.format(sbatch_source, sbatch_destination, pop + 1))
        
        for line in fileinput.input('{0}/sbatch_template_{1}.sh'.format(sbatch_destination, pop + 1), inplace=1):
            print(line.replace("su2_config_0.cfg", "su2_config_{0}.cfg".format(pop + 1)).rstrip())
            
        for line in fileinput.input('{0}/sbatch_template_{1}.sh'.format(sbatch_destination, pop + 1), inplace=1):
            print(line.replace("ge0_w0", "ge{0}_w{1}".format( gen, pop + 1 )).rstrip())
