source $HOME/.bashrc
conda activate tensorflow-gpu

ngpus=1

time legate --profile --cpus 16 \
		--gpus ${ngpus} --sysmem 256000 \
		--fbmem 16000 \
		--eager-alloc-percentage 10 \
		--mem-usage matmul.py