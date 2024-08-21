#!/bin/bash

#PBS -P p00
#PBS -q dgxa100
#PBS -l ncpus=16
#PBS -l ngpus=1
#PBS -l mem=32GB
#PBS -l walltime=00:05:00
#PBS -l wd

legate --profile --cpus 16 \
    --gpus 4 --sysmem 100000 \
    --fbmem 39000 \
    --eager-alloc-percentage 10 \
    --mem-usage matmul.py