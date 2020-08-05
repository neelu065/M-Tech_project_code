#!/bin/bash

#SBATCH --job-name dep_1_time   ##name that will show up in the queue
##SBATCH --nodes 1  ##number of nodes to use
#SBATCH --time 2-0:0:00  ##time for analysis (day-hour:min:sec)
##SBATCH --ntasks 1  ##number of tasks (analyses) to run
##SBATCH --cpus-per-task 20  ##the number of threads the code will use
#SBATCH --requeue  ##requeue when preempted and on node failure
#SBATCH --partition iist2
#SBATCH --nodes=1 --exclusive=user
## Load modules, insert code, and run your programs here.


echo "Sleeping time for compute node, while master node become active" 


rm -f slurm-$SLURM_JOB_ID.out

sleep 172700



