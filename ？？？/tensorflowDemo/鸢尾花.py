from sklearn.datasets import load_iris
import tensorflow as tf
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

# 总流程
# 准备数据
# 搭建网络
# 参数优化
# 测试效果

# 数据集读入
x_data = load_iris().data
y_data = load_iris().target

# 数据乱序
np.random.seed(116)
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(116)

# 区分数据集和训练集
x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

x_train = tf.cast(x_train, tf.float32)
y_train = tf.cast(y_train, tf.float32)
# 数据配对 [输入特征，标签]对 ， 每次喂入一批量 （batch）
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

# 定义神经网络所有可训练参数
w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))

lr = 0.1
train_loss_results = []
test_acc = []
epoch = 500
loss_all = 0

# 训练部分

# 嵌套循环迭代，with结构更新参数，显示当前loss
# 数据集级别迭代
for epoch in range(epoch):
    # batch级别迭代
    for step, (x_train, y_train) in enumerate(train_db):
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train, w1) + b1
            y = tf.nn.softmax(y)
            print(y)
            y_ = tf.one_hot(y_train, depth=3)
            # loss = tf.reduce_mean(tf.square(y_ - y))
            # loss_all += loss.numpy()
        # # 计算梯度
        # grads = tape.gradient(loss, [w1, b1])
#
#         w1.assign_sub(lr * grads[0])
#         b1.assign_sub(lr * grads[1])
#     print(f"epoch{epoch},loss{loss_all / 4}")
#     train_loss_results.append(loss_all / 4)
#     loss_all = 0

    # 测试部分
    # total_correct, total_number = 0, 0
    # for x_test, y_test in test_db:
    #     y = tf.matmul(x_test, w1) + b1
    #     y = tf.nn.softmax(y)
    #     pred = tf.argmax(y, axis=1)
    #     pred = tf.cast(pred, dtype=y_test.dtype)
    #     correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
    #     correct = tf.reduce_sum(correct)
    #     total_correct += int(correct)
    #     total_number += x_test.shape[0]
    # acc = total_correct / total_number
    # test_acc.append(acc)
    # print('test_acc', acc)
    # print('----------------')

# plt.title('Loss function curve')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.plot(train_loss_results, label="loss")
# plt.legend()
# plt.show()
#
# plt.title('Acc Curve')
# plt.xlabel('epoch')
# plt.ylabel('Acc')
# plt.plot(test_acc, label='accuracy')
# plt.legend()
# plt.show()
