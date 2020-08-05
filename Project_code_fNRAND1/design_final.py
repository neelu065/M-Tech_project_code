#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:34:13 2020

@author: neelu
"""

import concurrent.futures
import numpy as np


def design_point(path, target_vector, j=0):
    with open('{}/solution_final/design_vector/design_point_{}.txt'.format(path, j), 'w') as f:
        for i in range(len(target_vector)):
            np.savetxt(f, target_vector[i], fmt='%5.6f')


def restart_design_point(path, j):
    with open('{}/solution_final/design_vector/design_point_{}.txt'.format(path, j)) as f:
        data = np.loadtxt(f)

    def solution(i):
        vector = []
        """
            He
            """
        for j in range(len(data[0])):
            vector.append(data[i, j])
        return np.asarray([vector])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        iterator = range(len(data))
        results = executor.map(solution, iterator)

    target = [result for result in results]

    return target
