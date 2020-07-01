import tensorflow as tf
import numpy as np

# 张量类似矩阵 可以表示0阶到n阶的数组
# a = tf.constant([[1, 2], [3, 4]], dtype=tf.int64)
# print(a)
# print(a.dtype)
# print(a.shape)

# a = np.arange(9).reshape((3, 3))
# res = tf.convert_to_tensor(a, dtype=tf.int64)
# print(res)

# ret = tf.fill((1, 2), 9)
# print(ret)

# res = tf.cast(res, dtype=tf.float64)
# print(res)
#
# print(tf.reduce_max(res, axis=1))
# print(tf.reduce_min(res, axis=0))
#
# print(tf.reduce_mean(res, axis=1))
# print(tf.reduce_sum(res, axis=0))


# 将变量标记为可训练的 标记训练参数
# a = tf.Variable(tf.random.uniform((2, 2), minval=1, maxval=2))
# b = tf.Variable(tf.random.normal((2, 2), mean=0, stddev=1))
# print(a)
# print(b)
# print('----')
# print(tf.add(a, b))
#
# a = np.array([1, 2])
# b = np.array([[3], [4]])
#
# a = tf.constant(tf.convert_to_tensor(a))
# b = tf.constant(tf.convert_to_tensor(b))
# print(a)
# a = tf.reshape(a, (1, 2))
# print('---------')
# print(a)
# print(b)

# print(tf.matmul(a,b))


# 向神经网络传入数据
# features = tf.constant([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# lables = tf.constant([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
#
# data = tf.data.Dataset.from_tensor_slices((features, lables))
# # print(data)
#
# for element in data:
#     print(element)

# with tf.GradientTape() as tape:
#     w = tf.Variable(tf.constant(3.0, dtype=tf.float64))
#     loss = tf.pow(w, 4)
#
# grad = tape.gradient(loss, w)
# print(grad)

# a = tf.constant(10)
# a = tf.Variable(a)
# a.assign_sub(1)
# print(a)


# 归一化函数
a = tf.constant([1.01, 2.01, -0.66])
ret = tf.nn.softmax(a)
print(ret)
