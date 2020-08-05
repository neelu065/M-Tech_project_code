#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:43:49 2020

@author: neelu
"""

import os
from constrain import const_violation


def selection(target, trial, fobj_trial, fobj_target, Cmx_target, Cmx_trial, path):
    """
    This module take care of any external  constraint 
    that are not yet implement in the entire process.
    
    And the selection process take place according
    with deb and saha feasibility rules.
    
    """

    for i in range(len(target)):

        phi_a = const_violation(Cmx_target[i])  # phi_a corr to target vector
        phi_b = const_violation(Cmx_trial[i])  # phi_b corr to trial vector

        # domination criteria
        q1 = (phi_a == 0 and phi_b == 0)
        q2 = fobj_trial[i] < fobj_target[i]

        r1 = (phi_b == 0)
        r2 = phi_a > 0

        s1 = (phi_b < phi_a)
        s2 = phi_a > 0 and phi_b > 0

        if (q1 and q2) or (r1 and r2) or (s1 and s2):
            fobj_target[i] = fobj_trial[i]
            target[i] = trial[i]
            Cmx_target[i] = Cmx_trial[i]

            os.system('cp {}/mesh_files/wing_{}.su2 {}/solution_final/mesh_files'.format(path, i + 1, path))
            os.system(
                'cp {}/su2_solution_files/history_files/history_{}.csv {}/solution_final/history_files'.format(path,
                                                                                                               i + 1,
                                                                                                               path))
            os.system(
                'cp {}/su2_solution_files/restart_files/restart_flow_{}.dat {}/solution_final/restart_files'.format(
                    path, i + 1, path))

    return fobj_target, target, Cmx_target
