#!coding=utf-8

"""
    复数的数学运算
"""

# 复数可以使用complex(real,imag)或者是带有后缀j的浮点数来指定
a = complex(2, 4)
b = 3 - 5j
print a
print b

# 对应实部和虚部和共轭复数都很容易获取
print a.real  # 实部
print a.imag  # 虚部
print a.conjugate()  # 共轭复数

# 也支持数学运算
print a + b
print a * b
print a / b
print abs(a)

# 如果需要执行其他的复数函数比如正弦、余弦或平方根，使用cmath模块
import cmath
print cmath.sin(a)
print cmath.cos(a)
print cmath.exp(a)


# python的标准数学函数不能产生复数,如
# import math
# print sqrt(-1)  # 会报错

# 如果要产生复数，则必须使用cmathm模块，
print cmath.sqrt(-1)  # 1j
