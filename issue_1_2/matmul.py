import tensorflow as tf
import cunumeric as np
from legate.timing import time

tf.debugging.set_log_device_placement(True)
print('GPU devices: ', tf.config.list_physical_devices('GPU'))

steps = 10

size = 20000

A = tf.random.uniform(shape = [size, size])
B = tf.random.uniform(shape = [size, size])

# tensorflow
tf_elapsed = 0.0
for i in range(steps):
    start = time()
    C_1 = tf.linalg.matmul(A, B)
    tf_elapsed += time() - start

tf_elapsed /= steps


cu_elapsed_1 = 0.0
cu_elapsed_2 = 0.0
cu_elapsed_3 = 0.0
cu_elapsed_4 = 0.0
load_elapsed = 0.0
store_elapsed = 0.0

for i in range(steps):
    # 1
    # directly use tensors
    start = time()
    C_2 = np.matmul(A, B)
    cu_elapsed_1 += time() - start

    # 2
    # use .numpy() objects
    start = time()
    C_2 = np.matmul(A.numpy(), B.numpy())
    cu_elapsed_2 += time() - start

    # 3
    # load numpy() from tensors
    start = time()
    A1 = A.numpy()
    B1 = B.numpy()
    load_elapsed += time() - start
    # compute use the loaded numpy objects
    start = time()
    C_3 = np.matmul(A1, B1)
    cu_elapsed_3 += time() - start

    # 4
    # store numpy objects to cunumeric objects
    start = time()
    A2 = np.array(A1)
    B2 = np.array(B1)
    store_elapsed += time() - start
    # compute uses cunumeric objects
    start = time()
    C_4 = np.matmul(A2, B2)
    cu_elapsed_4 += time() - start

cu_elapsed_1 /= steps
cu_elapsed_2 /= steps
cu_elapsed_3 /= steps
cu_elapsed_4 /= steps
load_elapsed /= steps
store_elapsed /= steps

# print results
print('Tensorflow: ', tf_elapsed, ' ms')
print('cu 1: ', cu_elapsed_1, ' ms')
print('cu 2: ', cu_elapsed_2, ' ms')
print('cu 3: ', cu_elapsed_3, ' ms')
print('numpy(): ', load_elapsed, ' ms')
print('np.array(): ', store_elapsed, ' ms')
print('cu 4: ', cu_elapsed_4, ' ms')
print('numpy() + np.array() + cu 4: ', load_elapsed + store_elapsed + cu_elapsed_4, ' ms')