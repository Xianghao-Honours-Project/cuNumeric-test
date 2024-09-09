import tensorflow as tf

tf.debugging.set_log_device_placement(True)
print('GPU devices: ', tf.config.list_physical_devices('GPU'))

# 3.2 GB
size = 20000

A = tf.random.uniform(shape = [size, size])
B = tf.random.uniform(shape = [size, size])

C = tf.linalg.matmul(A, B)