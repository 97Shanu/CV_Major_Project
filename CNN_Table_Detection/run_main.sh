#!/bin/bash

#SBATCH --job-name=dlops_lab_7
#SBATCH --partition=gpu2
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

#SBATCH --gres=gpu

#SBATCH --output=test_%j.log


# module load python/3.7
module load anaconda/3
# python --version


#<Executable PATH> INPUT OUTPUT

python table_detection.py