import os


def delete_slurm_out_files():
    
    """
    As the name suggest This module will delete
    the slurm_out files generated at every generations.
    """

    for root, dirs, files in os.walk(".", topdown=False):
        for fi in files:
            if fi.endswith(".out"):
                os.system('rm -f {}'.format(fi))
            if fi.endswith(".vtk"):
                os.system('rm -f {}'.format(fi))

