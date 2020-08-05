import numpy as np


def mutation_crossover(population_size, target, cross_over_prob, singular_values_selected, mut):
    
    """
    
    This module will cover the mutation and crossover stages of fNRAND1.
    
    Along with this it is also noted  due to mutation and crossover 
    there is possiblilty that the trial vector may run out of design space.
    To bring it back to same space, np.clip module is used.
    
    Input : as mentioned above.
    Output : trail vector.

    """

    trial = []

    for j in range(population_size):

        # Mutation
        ind_vector = [idx for idx in range(population_size) if idx != j]  # check to make sure that own index is not
        # selected

        vector = []
        for n in ind_vector:
            ind_sum = np.sum((target[j] - target[n]) ** 2)
            vector.append(ind_sum)
        ind = np.argmin(vector)

        a = target[ind]

        inter_med = np.random.choice(ind_vector, 2,
                                     replace=False)  # here only two position vector are randomly selected in nature

        b = target[inter_med[0]]
        c = target[inter_med[1]]

        mutant = a + mut * (b - c)

        # Cross-over
        cross_points = np.random.rand(singular_values_selected) < cross_over_prob  # result in boolean values
        
        if not np.any(cross_points):  # check for false value
            cross_points[
                np.random.randint(0, singular_values_selected)] = True  # Forcing atleast one index to become true.
        
        trial_scalar = np.where(cross_points, mutant, target[j])  # trial vector generator
        
        trial.append(trial_scalar)

    with open('optimizer_input/design_range.csv') as f:
        data = np.loadtxt(f)
    design_space = data[0: singular_values_selected].T

    negative_limit = design_space[0]
    positive_limit = design_space[1]
    
    trial = np.clip(trial, negative_limit, positive_limit)  # This will clip the values to boundary value in given design space.

    return trial
