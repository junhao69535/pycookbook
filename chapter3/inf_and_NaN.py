#!coding=utf-8

"""
    无穷大与NaN
"""

# 创建或测试正无穷、负无穷或NaN（非数字）的浮点数
# 可以使用float()来创建
a = float('inf')  # 正无穷
b = float('-inf')  # 负无穷
c = float('nan')
print a, b, c

# 为了测试这些值的存在，使用math.isinf()和math.isnan()函数
import math
print math.isinf(a)
print math.isnan(c)

# 无穷大数在执行数学计算的时候会传播
a = float('inf')
print a + 45  # inf
print a * 10  # inf
print 10 / a  # 0.0

# 但有些未定义的操作会返回一个NaN结果
print a / a  # NaN
print a + b  # NaN


# NaN值的一个特别的地方是它们之间的比较操作总是返回False，
d = float('nan')
print c == d  # False
print c is d  # False

# 因此，测试一个NaN值的唯一安全的方法就是math.isnan()
