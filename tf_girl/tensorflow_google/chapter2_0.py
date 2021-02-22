# -*- encoding: utf-8 -*-
# @File:   chapter2_0.py    
# @Time: 2020-10-09 22:04
# @Author: ZHANG
# @Description: chapter2_0

import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b
sess = tf.compat.v1.Session()
print(sess.run(result))

print(a.graph is tf.get_default_graph())
