#!coding=utf-8

"""
    矩阵与线性代数运算
"""

# 使用numpy库可以解决
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 7, -9]])
print m
print m.T  # 矩阵m的转置
print m.I  # 求逆矩阵
v = np.matrix([[2], [3], [4]])
print m * v  # 矩阵相乘


# 更多内容请访问官网