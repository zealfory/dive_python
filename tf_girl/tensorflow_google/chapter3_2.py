# -*- encoding: utf-8 -*-
# @File:   chapter3_2.py    
# @Time: 2020-10-09 23:45
# @Author: ZHANG
# @Description: chapter3_2

import tensorflow as tf

w1 = tf.Variable(tf.random_normal((2, 3), stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal((3, 1), stddev=1, seed=1))

x = tf.constant([[0.7, 0.9]])

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
    # tf.global_variables_initializer().run()
    sess.run(tf.global_variables_initializer())
    print(sess.run(y))

