# -*- encoding: utf-8 -*-
# @File:   batch_norm.py    
# @Time: 2020-08-20 14:41
# @Author: ZHANG
# @Description: batch_norm

 
m = K.mean(X, axis=-1, keepdims=True)  # 计算均值
std = K.std(X, axis=-1, keepdims=True)  # 计算标准差
X_normed = (X - m) / (std + self.epsilon)  # 归一化
out = self.gamma * X_normed + self.beta  # 重构变换