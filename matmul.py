import numpy as np

size = 50000

A = np.random.randn(size, size)
B = np.random.randn(size, size)

np.matmul(A, B)