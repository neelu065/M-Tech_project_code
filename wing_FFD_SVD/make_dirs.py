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

    os.mkdir('{}'.format(path))
    os.mkdir('{}/perturbed_cp'.format(path))
    os.mkdir('{}/perturbed_wing'.format(path))
    os.mkdir('{}/perturbed_wing/format_wing'.format(path))
    os.mkdir('{}/perturbed_wing/unformat_wing'.format(path))
