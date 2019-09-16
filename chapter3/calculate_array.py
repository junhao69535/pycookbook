#!coding=utf-8

"""
    大型数组运算
"""

# 涉及数组的重量级运算操作，可以使用NumPy库。
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print x * 2  # [1, 2, 3, 4, 1, 2, 3, 4]
# print x + 10  # 会报错，只有列表之间才能相连接
print x + y

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print ax * 2  # array([2, 4, 6, 8])
print ax + 10  # array([11, 12, 13, 14])
print ax + ay  # array([ 6, 8, 10, 12])
print ax * ay  # array([ 5, 12, 21, 32])

# 更深入的内容可以到numpy官网了解