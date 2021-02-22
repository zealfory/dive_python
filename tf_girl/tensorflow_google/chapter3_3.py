# -*- encoding: utf-8 -*-
# @File:   chapter3_3.py    
# @Time: 2020-10-12 00:36
# @Author: ZHANG
# @Description: chapter3_3

import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(1, 2), name='input')
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

# print(sess.run(y))  # tensorflow.python.framework.errors_impl.InvalidArgumentError:
# You must feed a value for placeholder tensor 'input' with dtype float and shape [1,2]

print(sess.run(y, feed_dict={x: [[0.7, 0.9]]}))

