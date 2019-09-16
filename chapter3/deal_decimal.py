#!coding=utf-8

"""
    执行精确的浮点数运算
"""

# 当需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
# 浮点数的一个普遍问题时它们并不能精确的表示十进制数。并且即使是最简单的舒徐运算也会产生小的误差
a = 4.2
b = 2.1
print a + b  # 这里print会处理a+b，实际上a+b返回的是6.300000000000001
print (a + b) == 6.3  # 这里返回False就可以知道a+b不等于6.3

# 这些错误是由底层CPU和IEEE 754标准通过自己的浮点单位去执行算术时的特征。由于python
# 的浮点数据类型使用底层表示存储属于，因此没有办法避免。

# 如果想更加精确，且能容忍一定的性能损耗，可以使用decimal模块
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
# Decimal 对象会像普通浮点数一样的工作(支持所有的常用数学运算)
print a + b
print (a + b) == Decimal('6.3')


# decimal 模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍五入运算。
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print a / b
with localcontext() as ctx:
    ctx.prec = 3  # 利用上下文把位数精确到3
    print a / b

with localcontext() as ctx:
    ctx.prec = 50  # 利用上下文把位数精确到50
    print a / b


# 如果不追求精确，使用原生浮点运算性能会更好。
# 但并不代表完全忽略误差，如下：
nums = [1.23e+18, 1, -1.23e+18]
print sum(nums)  # 得到0
# 上面错误可以利用math.fsum()提供更精确的计算能力解决：
import math
print math.fsum(nums)  # 得到1

# 总结，decimal主要用在涉及金融的领域。