legate --profile --cpus 16 \
    --gpus 4 --sysmem 100000 \
    --fbmem 39000 \
    --eager-alloc-percentage 10 \
    --mem-usage matmul.py