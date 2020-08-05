#!/bin/bash

#SBATCH --job-name ge0_w0   ##name that will show up in the queue
#SBATCH --nodes 1  ##number of nodes to use
#SBATCH --time 0-04:0:00  ##time for analysis (day-hour:min:sec)
#SBATCH --ntasks 1  ##number of tasks (analyses) to run
#SBATCH --cpus-per-task 1  ##the number of threads the code will use
#SBATCH --requeue  ##requeue when preempted and on node failure
##SBATCH -licenses=pwid_LICENSE
#SBATCH --partition iist
##SBATCH --nodelist=cn15
## Load modules, insert code, and run your programs here.

/scratch/neelappagouda/SU2_V-7.0/bin/SU2_CFD optimizer_output/su2_config_files/su2_config_0.cfg



