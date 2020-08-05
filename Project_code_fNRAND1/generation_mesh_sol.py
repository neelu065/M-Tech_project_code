import os
import concurrent.futures
from sbatch_file import sbatch_file
from re_mut_cross import re_mutation_crossover
from re_wing_re_generator_iter import re_wing_regenerator_iter


def gen_mesh_solution(trail_vector, population_size, pw_path, sbatch_destination, perturbed_wing_file_path, gen_number, target_vector, cross_over_prob, mut, singular_values_selected):
   
    """
    This module will mesh over newly generated wings,
    followed by SU2_CFD solution.
    """
    
    sbatch_file(population_size, gen_number)
    
    def gen_meshing_solution(i):
        
        """
        This module will create the mesh files (*.su2) using pointwise.
        
        And is place in while loop with the intention to eliminate the 
        wrinkled wing surfaces.
        """
        
        command = '{}/pointwise -b {}/pointwise_template_{}.glf'.format(pw_path, perturbed_wing_file_path, i)
        os.system(command)
        
        trial = trail_vector[i - 1]

        while not os.path.isfile('optimizer_output/mesh_files/wing_{}.su2'.format(i)):
            
            trial = re_mutation_crossover(population_size, target_vector, cross_over_prob, singular_values_selected, mut, i-1)
    
            re_wing_regenerator_iter(trial, singular_values_selected, i)
            
            command = '{}/pointwise -b {}/pointwise_template_{}.glf'.format(pw_path, perturbed_wing_file_path, i)
            os.system(command)
            
        print('wing_{}.su2 file created ...'.format(i))
        
        return trial

    with concurrent.futures.ThreadPoolExecutor() as executor:
        iterator = range(1, population_size + 1)
        results = executor.map(gen_meshing_solution, iterator)  # map func will output the results (value) in the same sequence.

    return results
