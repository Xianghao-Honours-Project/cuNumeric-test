import cunumeric as np
from  legate.timing import time

size = 20000

A = np.random.randn(size, size)
B = np.random.randn(size, size)


iters = 10
steps = 10
for j in range(iters):
    total = 0.0
    for i in range(steps):
        start = time()
        np.matmul(A, B)
        total += time() - start
    print("Matmul time: ", total / steps)
