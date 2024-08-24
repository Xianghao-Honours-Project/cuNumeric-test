#!/bin/bash

#PBS -P es56
#PBS -q dgxa100
#PBS -l ncpus=64
#PBS -l ngpus=4
#PBS -l mem=256GB
#PBS -l walltime=00:05:00
#PBS -l wd
#PBS -l storage=scratch/p00
#PBS -j oe

__conda_setup="$('/scratch/p00/xw6261/libraries/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/scratch/p00/xw6261/libraries/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/scratch/p00/xw6261/libraries/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/scratch/p00/xw6261/libraries/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup

conda activate legate

legate --profile --cpus 16 \
    --gpus 4 --sysmem 100000 \
    --fbmem 39000 \
    --eager-alloc-percentage 10 \
    --mem-usage matmul.py

