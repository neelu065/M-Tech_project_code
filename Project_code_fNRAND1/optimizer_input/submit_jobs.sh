#!/bin/bash

#SBATCH --job-name gener_0   ##name that will show up in the queue
#SBATCH --nodes 1  ##number of nodes to use
#SBATCH --time 0-05:0:00  ##time for analysis (day-hour:min:sec)
#SBATCH --ntasks 4  ##number of tasks (analyses) to run
#SBATCH --cpus-per-task 1  ##the number of threads the code will use
#SBATCH --requeue  ##requeue when preempted and on node failure
#SBATCH --partition iist2
#SBATCH --nodelist cn17
#SBATCH --exclusive=user
##SBATCH ## meant for dependency line
## Load modules, insert code, and run your programs here.

population_size=4
sbatch_destination=optimizer_output/sbatch_template_files

python mesh_file_signal.py $population_size
python submit_jobs.py $population_size $sbatch_destination

rm -f slurm-$SLURM_JOB_ID.out

sleep 200
