import time
import os
from script_wait import squeue_file
from delete_slurm_files import delete_slurm_out_files


def sleep_time(wait, short_sleep):
    
    """
    This module is designed to balance the buffer
    between master and compute node.

    Also, this will eliminate the squeue.csv, slurm-{}.out files
    which were generated due to usage of squeue and sbatch commands.
    """

    while wait == "Yes":
        wait = squeue_file(short_sleep, "No")

    time.sleep(short_sleep)

    os.system('rm -f squeue_file.csv')

    delete_slurm_out_files()

    print("All Jobs Executed ...")
