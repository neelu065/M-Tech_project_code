#!/bin/bash

#SBATCH --job-name optimizer   ##name that will show up in the queue
#SBATCH --nodes 1  ##number of nodes to use
#SBATCH --time 0-02:0:00  ##time for analysis (day-hour:min:sec)
#SBATCH --ntasks 1  ##number of tasks (analyses) to run
#SBATCH --cpus-per-task 1  ##the number of threads the code will use
#SBATCH --requeue  ##requeue when preempted and on node failure
#SBATCH --mail-user neelu065@gmail.com  ##your email address
##SBATCH --license=pwid_LICENSE
#SBATCH --partition iist-all
## Load modules, insert code, and run your programs here.
#SBATCH --nodes=1 --exclusive
time python run_optimizer.py 