#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:05:27 2020

@author: neelappagouda
"""

import os
import sys
from delete_slurm_files import delete_slurm_out_files


def delete_files(path):
    """
    As the name suggests this module will clear
    the previously created folder.
    """

    if os.path.exists(path):

        data = input('Previously generated output file exists ! \n\nDo you want to proceed by rewriting those files ?\n\nType "Yes" to proceed, else "No" to exit:')

        if data=="Yes":
            os.system('rm -rf {}'.format(path))
        else:
            print('\nExiting ...')
            sys.exit()

    delete_slurm_out_files()


