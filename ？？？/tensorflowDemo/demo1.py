import tensorflow as tf
import numpy as np

# 设定迭代初始值为5
w = tf.Variable(tf.constant(5, dtype=tf.float32))
# 学习率
lr = 0.2
# 循环迭代40次
epoch = 40


for i in range(epoch):
    with tf.GradientTape() as tape:
        # 损失函数 f = （w+1）**2
        loss = tf.square(w + 1)
    # gradient函数告知谁对谁求导 loss 函数对 w求导数
    grads = tape.gradient(loss, w)
    # w自减 相当于 w -= lr*grads
    w.assign_sub(lr * grads)

    print(i, w.numpy(), loss)
