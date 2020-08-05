import numpy as np
from re_wing_generator import re_wing_generator


def re_wing_regenerator_iter(trial, sigma_selected, i):
    with open('optimizer_input/matrix_vh.csv') as g:
        g = np.loadtxt(g)
        vh = g[: sigma_selected, :]

    X_matrix = np.matmul(trial, vh)

    for _ in range(len(X_matrix)):
        re_wing_generator(X_matrix, i)  # This module will create the wings and place them at respective position.
