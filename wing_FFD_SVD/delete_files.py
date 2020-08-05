#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:05:27 2020

@author: neelappagouda
"""

import os


def delete_files(path):
    """
    As the name suggests this module will clear
    the previously created folder.
    """

    if os.path.exists(path):
        os.system('rm -rf {}'.format(path))

