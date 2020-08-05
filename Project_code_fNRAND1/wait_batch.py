import os


def wait_batch():
    os.system('sbatch compute_wait.sh')