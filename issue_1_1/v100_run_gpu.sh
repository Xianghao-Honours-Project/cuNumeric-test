source $HOME/.bashrc
conda activate tensorflow-gpu

ngpus=4

time legate --profile --cpus 16 \
		--gpus ${ngpus} --sysmem 256000 \
		--fbmem 26000 \
		--eager-alloc-percentage 10 \
		--mem-usage test.py
