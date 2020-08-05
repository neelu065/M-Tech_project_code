import pandas as pd
import time
import os
import getpass

user = getpass.getuser()


def squeue_file(short_sleep, wait):
    os.system('squeue &> squeue_file.csv')
    with open('squeue_file.csv') as f:
        sqeue_data = pd.DataFrame(f)

    sqeue_intermediate = []

    for row in range(len(sqeue_data)):
        va = sqeue_data.iat[row, 0].split()
        if va[3].startswith(user[:4]):  # To extract my JOB_ID
            sqeue_intermediate.append(va[0])

    squeue_JOB_IDs = []

    for j in range(len(sqeue_intermediate)):
        squeue_JOB_IDs.append([int(data) for data in sqeue_intermediate[j].split() if data.isdigit()])
    # print('squeue = {}'.format(squeue_JOB_IDs))

    for root, dirs, files in os.walk(".", topdown=False):
        # print('files present = {}'.format(files))
        slurm_out_files = [fi for fi in files if fi.endswith(".out")]

    slurm_out_files_IDs = []
    for j in range(len(slurm_out_files)):
        abc = slurm_out_files[j]
        number = abc[6:-4].split()
        number = [int(i) for i in number if i.isdigit()]
        slurm_out_files_IDs.append(number)
    # print('slurm_out_files = {}'.format(slurm_out_files_IDs))

    for sqeue_JOB_ID in squeue_JOB_IDs:
        if wait == "No":
            for slurm_out_files_ID in slurm_out_files_IDs:

                if slurm_out_files_ID == sqeue_JOB_ID:
                    wait = "Yes"
                    print("Your Jobs are in progress ...")
                    break
        else:
            break

    if wait == "Yes":
        time.sleep(short_sleep)

    return wait



