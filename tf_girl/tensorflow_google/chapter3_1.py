# -*- encoding: utf-8 -*-
# @File:   chapter3_1.py    
# @Time: 2020-10-09 22:53
# @Author: ZHANG
# @Description: chapter3_1

import tensorflow as tf
# tf.constant 是一个计算，这个计算的结果是一个张量，保存在变量a中
# 张量并不是数组形式，它只是对TensorFlow中运算解果的引用
a = tf.compat.v1.constant([1.0, 2.0], name="a")
# a = tf.compat.v1.constant([1, 2], name="a")  # TypeError: Input 'y' of 'Add' Op has type float32 that
# does not match type int32 of argument

print(a)  # Tensor("a:0", shape=(2,), dtype=float32)


b = tf.compat.v1.constant([2.0, 3.0], name="b")

# result = a + b
result = tf.compat.v1.add(a, b, name="add")
print(result)
