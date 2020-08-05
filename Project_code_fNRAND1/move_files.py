import os
from delete_slurm_files import delete_slurm_out_files


def move_files(path, i=0):
    """
    
    This module move the important solution files
    into generation folder.
    It set the platform for final_solution files.
    Also it will *.tar files and remove original files.
    
    """

    os.mkdir('{}/generation_sol_files/gen_{}'.format(path, i))

    gen_folder_path = '{}/generation_sol_files/gen_{}'.format(path, i)

    os.mkdir('{}/mesh_files'.format(gen_folder_path))
    os.system('mv {}/mesh_files/* {}/mesh_files'.format(path, gen_folder_path))

    os.mkdir('{}/restart_files'.format(gen_folder_path))
    os.system('mv {}/su2_solution_files/restart_files/* {}/restart_files'.format(path, gen_folder_path))

    os.mkdir('{}/history_files'.format(gen_folder_path))
    os.system('mv {}/su2_solution_files/history_files/* {}/history_files'.format(path, gen_folder_path))

    os.system('mv {}/fobj_{}.csv {}/generation_sol_files/obj_func'.format(path, i, path))

    delete_slurm_out_files()

    if i == 0:
        os.system('cp -r {}/* {}/solution_final'.format(gen_folder_path, path))

    print("Compressing gen_{} files".format(i))

    # Below line should always be at the end of this module.
    os.chdir('{}/generation_sol_files/'.format(path))
    os.system('tar -czf gen_{0}.tar gen_{1}/* && rm -rf gen_{2}'.format(i, i, i))
    os.chdir('../../')

    print("Deleting the gen_{} original files".format(i))
