import concurrent.futures
import os
import sys

a = float(sys.argv[1])
population_size = int(a)
sbatch_destination = sys.argv[2]


def solution(i):
    """
    Here this module will submit the jobs
    in parallel to compute nodes.
    """

    command = 'sh {0}/sbatch_template_{1}.sh'.format(sbatch_destination, i)
    os.system(command)


with concurrent.futures.ThreadPoolExecutor() as executor:
    iterator = range(1, population_size + 1)
    executor.map(solution, iterator)
