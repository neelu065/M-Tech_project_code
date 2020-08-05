#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 22:46:24 2020

@author: neelu
"""

import os
import fileinput


def template_copy_replace(pop_size):
    """
    This module will generate multiple config and template files
    and place them in respective destination.

    Then, these files are modified at certain places as shown below.
    """

    pw_temp_source = 'optimizer_input/pointwise_mesh_template.glf'
    pw_temp_dest = 'optimizer_output/pointwise_template_files'

    su2_config_source = 'optimizer_input/template.cfg'
    su2_config_dest = 'optimizer_output/su2_config_files'

    sbatch_source = 'optimizer_input/sbatch_template.sh'
    sbatch_destination = 'optimizer_output/sbatch_template_files'

    restart_file_source = 'optimizer_input/restart_naca.dat'
    restart_file_destination = 'optimizer_output/restart_naca_files'

    for i in range(pop_size):

        os.system('cp {0} {1}/pointwise_template_{2}.glf'.format(pw_temp_source, pw_temp_dest, i + 1))
        os.system('cp {0} {1}/su2_config_{2}.cfg'.format(su2_config_source, su2_config_dest, i + 1))
        os.system('cp {0} {1}/sbatch_template_{2}.sh'.format(sbatch_source, sbatch_destination, i + 1))
        os.system('cp {0} {1}/restart_naca_{2}.dat'.format(restart_file_source, restart_file_destination, i + 1))

        # Replacing the strings inside the pointwise_template_file begins
        for line in fileinput.input('{}/pointwise_template_{}.glf'.format(pw_temp_dest, i + 1), inplace=1):
            print(line.replace("wing_0", "wing_{}".format(i + 1)).rstrip())

        # Same as above, But with su2_config files.
        for line in fileinput.input('{0}/su2_config_{1}.cfg'.format(su2_config_dest, i + 1), inplace=1):
            print(line.replace("wing_0", "wing_{}".format(i + 1)).rstrip())

        for line in fileinput.input('{0}/su2_config_{1}.cfg'.format(su2_config_dest, i + 1), inplace=1):
            print(line.replace("history_0", "history_{}".format(i + 1)).rstrip())

        for line in fileinput.input('{0}/su2_config_{1}.cfg'.format(su2_config_dest, i + 1), inplace=1):
            print(line.replace("restart_flow_0", "restart_flow_{}".format(i + 1)).rstrip())

        for line in fileinput.input('{0}/su2_config_{1}.cfg'.format(su2_config_dest, i + 1), inplace=1):
            print(line.replace("restart_naca_0", "restart_naca_{}".format(i + 1)).rstrip())