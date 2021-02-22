# -*- encoding: utf-8 -*-
# @File:   chapter4_0.py    
# @Time: 2020-10-12 11:49
# @Author: ZHANG
# @Description: chapter4_0

import tensorflow as tf

v = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
with tf.Session() as sess:
    # clip_by_value func
    print(tf.clip_by_value(v, 2.5, 4.5).eval())

    # log func
    v = tf.constant([1.0, 2.0, 3.0])
    print(tf.log(v).eval())

    # * vs matmul
    v1 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    v2 = tf.constant([[5.0, 6.0], [7.0, 8.0]])

    print((v1 * v2).eval())
    print(tf.matmul(v1, v2).eval())


