# -*- encoding: utf-8 -*-
# @File:   chapter4_1.py    
# @Time: 2020-10-18 14:37
# @Author: ZHANG
# @Description: chapter4_1

import tensorflow as tf
v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
v2 = tf.constant([4.0, 3.0, 2.0, 1.0])

sess = tf.InteractiveSession()
print(tf.greater(v1, v2).eval())

print(tf.where(tf.greater(v1, v2), v1, v2).eval())
sess.close()
