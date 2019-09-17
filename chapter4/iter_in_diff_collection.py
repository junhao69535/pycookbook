#!coding=utf-8

"""
    不同集合上元素的迭代
"""


# 需要在多个对象执行相同的操作，但是这些对象在不同的容器里
# itertools.chain()方法可以简化这个任务，返回一个迭代器
from itertools import chain
a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = chain(a, b)  # 这个结合只会把key结合载一起，value会丢失
# 因为itertools.chain()不适用于dict
# collections.Chain可以结合映射对象，可是不支持python2

e = [1, 2, 3, 4]
f = {'x', 'y', 'z'}
for i in chain(e, f):
    print i