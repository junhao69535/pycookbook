#!coding=utf-8

"""
    可接受任意数量参数的函数
"""


# 为了能让一个函数接受任意数量的位置参数，可以使用一个*参数：
def avg(first, *rest):
    return float((first + sum(rest))) / (len(rest) + 1)


print avg(1, 2)
print avg(1, 2, 3, 4)


# 为了接受任意数量的关键字参数，使用一个以**开头的参数
def get_element(name, value, **attrs):
    print name, value
    for key, item in attrs.items():
        print key, item


get_element('name', 'value', jack=10, marry=20)
# 一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数
# 下面的例子都是错误的：
# def a(x, *args, y):
#     pass
#
# def b(x, *args, y, **kwargs):
#     pass