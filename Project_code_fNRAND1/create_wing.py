#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:55:54 2020

@author: neelu
"""

from random_design_space_generator import design_space
from wing_generator import wing_generator


def create_wing(singular_values_selected, pop_size, i):
    
    """
    This module generate the design variable and further
    create the wing equal to number of population size.
    
    Input:number of principal components selected and population size selected.
    Output: Wing generated with no wrinkles nor any unexpected shapes.
    """

    X_matrix, target = design_space(singular_values_selected, pop_size)  # Co_variance matrix created.

    wing_generator(X_matrix, i)  # perturbed wings created.

    return target
