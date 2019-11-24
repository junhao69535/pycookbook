#!coding=utf-8

"""
    简化数据结构的初始化
"""


# 写了很多仅仅用于数据结构的类，不想写太多__init__()函数
# 可以在一个基类中写一个公用的__init__()函数
import math


class Structure1(object):
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


s = Stock('ACME', 50, 91.1)
p = Point(2, 3)
c = Circle(4.5)