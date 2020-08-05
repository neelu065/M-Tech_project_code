#!/bin/bash

#SBATCH --job-name ping_time   ##name that will show up in the queue
#SBATCH --nodes 1  ##number of nodes to use
##SBATCH --time 4-0:0:00  ##time for analysis (day-hour:min:sec)
#SBATCH --ntasks 1  ##number of tasks (analyses) to run
#SBATCH --cpus-per-task 1  ##the number of threads the code will use
#SBATCH --requeue  ##requeue when preempted and on node failure
#SBATCH --partition iist2
##SBATCH --nodes=1 --exclusive=user
##SBATCH --nodelist=cn15
#SBATCH --qos=expedite
## Load modules, insert code, and run your programs here.


echo "Sleeping time for compute node, while master node become active" 

rm -f slurm-$SLURM_JOB_ID.out

sleep 100

echo "sleep over"


