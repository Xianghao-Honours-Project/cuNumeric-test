#!/bin/bash

#PBS -P es56
#PBS -q dgxa100
#PBS -l ncpus=128
#PBS -l ngpus=8
#PBS -l mem=256GB
#PBS -l walltime=00:10:00
#PBS -l wd
#PBS -l storage=scratch/p00
#PBS -j oe

source $HOME/.bashrc

conda activate legate

for ngpus in 1 2 4 6 8
do
	echo "########## run on ${ngpus} ########"
	
	echo legate --profile --cpus 16 \
                --gpus ${ngpus} --sysmem 100000 \
                --fbmem 39000 \
                --eager-alloc-percentage 10 \
                --mem-usage matmul.py

	legate --profile --cpus 16 \
    		--gpus ${ngpus} --sysmem 100000 \
    		--fbmem 39000 \
    		--eager-alloc-percentage 10 \
    		--mem-usage matmul.py
done
