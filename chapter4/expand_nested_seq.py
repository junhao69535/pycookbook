#!coding=utf-8

"""
    展开嵌套的序列
"""


# 想将一个多层嵌套序列展开成一个单层列表
# 可以使用一个包含yield from语句的递归生成器解决
from collections import Iterable


def flatten(items, ignore_types=(str, unicode)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for y in flatten(x):  # 本来这两条语句可以协程yield from faltten(x)
                yield y  # python2没有yield from语法，只能改成这样
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print x

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print x


# 语句 yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用。 如果
# 你不使用它的话，那么就必须写额外的 for 循环了。比如：
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x