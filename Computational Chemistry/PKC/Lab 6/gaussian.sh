#!/bin/bash
#BATCH -J g16-opt # name of the job
#SBATCH -o brch3cl.log
#SBATCH -p standard-low # name of the partition: available options "standard, standard-low, gpu, hm"
#SBATCH --exclusive
#SBATCH --nodes=1
#SBATCh --ntasks-per-node=20
#SBATCH -t 72:00:00 # walltime in HH:MM:SS, Max value 72:00:00
#list of modules you want to use, for example
module load apps/gaussian/16/gnu
#name of the executable
exe=g16
#run the application
$exe brch3cl.gjf
