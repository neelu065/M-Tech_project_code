import os
import time


def check_slurm_out_file(deep_sleep,short_sleep,wait = 1):

    """
        As the name suggest This module will check
        the slurm_out files, if any *.out is found, implies that
        job in compute node running and wait is set to 0.
        """

    while wait == 1:

        time.sleep(short_sleep)

        for root, dirs, files in os.walk(".", topdown=False):
            for fi in files:
                if fi.endswith(".out"):
                    slurm_file_name = '{}'.format(fi)
                    print("slurm_out file found")
                    wait = 0
                    break
                else:
                    wait = 1

    time.sleep(deep_sleep)

    wait = 1
    while wait == 1:
        time.sleep(short_sleep)

        if os.path.isfile(slurm_file_name):
            wait = 1
        else:
            wait = 0
