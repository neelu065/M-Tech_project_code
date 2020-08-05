import fileinput
import os
import time


def job_id_extract(job_id_file):
    time.sleep(1)
    with open(job_id_file) as f:
        li = f.readline()
    return int(li.split()[3])


def dependency_job_submit(path, generation, init_gen=0):
    if os.path.isfile('slurm*'):
        os.system('rm -f slurm*')

    if init_gen != 0:
        try:
            os.system('rm -f {}/mesh_files/*'.format(path))
        except:
            pass

    for i in range(init_gen, generation + 1):
        # if i == 0 or i == init_gen:
        #
        #     os.system('cp optimizer_input/submit_jobs.sh {}/sbatch_dependency_files/jobs_{}.sh'.format(path, i))
        #
        #     for line in fileinput.input('{}/sbatch_dependency_files/jobs_{}.sh'.format(path, i), inplace=1):
        #         print(line.replace("gener_0", "gener_{}".format(i)).rstrip())
        #
        #     os.system('sbatch {}/sbatch_dependency_files/jobs_{}.sh > job_{}.log &'.format(path, i, i))
        #     job_id = job_id_extract('job_{}.log'.format(i))
        #
        # else:
        os.system('cp optimizer_input/submit_jobs.sh {}/sbatch_dependency_files/jobs_{}.sh'.format(path, i))

        if i != init_gen:
            for line in fileinput.input('{}/sbatch_dependency_files/jobs_{}.sh'.format(path, i), inplace=1):
                print(line.replace("##SBATCH", "#SBATCH --dependency=afterok:{}".format(job_id)).rstrip())

        for line in fileinput.input('{}/sbatch_dependency_files/jobs_{}.sh'.format(path, i), inplace=1):
            print(line.replace("gener_0", "gener_{}".format(i)).rstrip())

        os.system('sbatch {}/sbatch_dependency_files/jobs_{}.sh > job_{}.log &'.format(path, i, i))

        job_id = job_id_extract('job_{}.log'.format(i))

    os.system('rm -f job*.log'.format(i))
