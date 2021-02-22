# -*- encoding: utf-8 -*-
# @File:   chapter3_0.py    
# @Time: 2020-10-09 22:41
# @Author: ZHANG
# @Description: chapter3_0

import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b
sess = tf.compat.v1.Session()
print(sess.run(result))

print(a.graph is tf.compat.v1.get_default_graph())


g1 = tf.Graph()
with g1.as_default():
    v = tf.compat.v1.get_variable(
        "v", shape=[1], initializer=tf.zeros_initializer
    )

g2 = tf.Graph()
with g2.as_default():
    v = tf.compat.v1.get_variable(
        "v", shape=[1], initializer=tf.ones_initializer
    )

with tf.compat.v1.Session(graph=g1) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("", reuse=True):
        print(sess.run(tf.compat.v1.get_variable("v")))


with tf.compat.v1.Session(graph=g2) as sess:
    tf.compat.v1.global_variables_initializer().run()
    with tf.compat.v1.variable_scope("", reuse=True):
        print(sess.run(tf.compat.v1.get_variable("v")))

# 制定计算运行的设备
g = tf.compat.v1.Graph()
with g.device('/gpu:0'):
    result = a + b
# sess = tf.compat.v1.Session()
# print(sess.run(result))
