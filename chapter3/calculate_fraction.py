#!coding=utf-8

"""
    分数计算
"""

# fractions模块可以解决分数运算问题
from fractions import Fraction
a = Fraction(5, 4)  # 5/4
b = Fraction(7, 16)  # 7/16
print a + b
print a * b

c = a * b
# 获取分子
print c.numerator
# 获取分母
print c.denominator
# 转换成浮点型
print float(c)
# 限制分母的值，会取约等于数，使得分母尽可能接近给出的参数
print c.limit_denominator(8)
# 把一个浮点型数转换成分数
x = 3.75
y = Fraction(*x.as_integer_ratio())
print y