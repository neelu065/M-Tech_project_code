import numpy as np
from wing_generator import wing_generator


def wing_regenerator_iter(trial, sigma_selected):
    
    """
    Here trial vector is multiplied 
    to all principal modes selected.
    """
    
    with open('optimizer_input/matrix_vh.csv') as g:
        g = np.loadtxt(g)
        vh = g[: sigma_selected, :]

    X_matrix = np.matmul(trial, vh)

    for j in range(len(X_matrix)):
        wing_generator(X_matrix[j], j + 1)  # This module will create the wings and place them at respective position.
