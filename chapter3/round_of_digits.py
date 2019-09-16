#!coding=utf-8

"""
    数字的四舍五入
"""

# 想对浮点数执行指定精度的舍入运算
# 对于简单的舍入运算，使用内置的round(value, ndigits)即可
print round(1.23, 1)  # 保留一位
print round(1.27, 1)  # 会进行四舍五入
print round(-1.27, 1)
print round(1.25361, 3)  # 保留三位

# 传给ndigits参数可以是负数，这时，舍入运算会作用在十位、百位、千位等上面
a = 1627731
print round(a, -1)
print round(a, -2)
print round(a, -3)


# 如果不允许小误差，需要使用decimal模块