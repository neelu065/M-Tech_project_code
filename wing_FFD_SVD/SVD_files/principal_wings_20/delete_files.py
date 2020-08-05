#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:05:27 2020

@author: neelappagouda
"""

import os


def delete_files():
    """
    As the name suggests this module will clear
    the previously created folder.
    """

    if os.path.exists('principal_wings'):
        os.system('rm -rf principal_wings')

    if os.path.exists('random_wings'):
        os.system('rm -rf random_wings')



