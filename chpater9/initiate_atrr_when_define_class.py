#!coding=utf-8
"""
    再定义的时候初始化类的成员
"""
# 你想在类被定义的时候就初始化一部分类的成员，而不是要等到实例被创建后。
# 在类定义时就执行初始化或设置操作是元类的一个典型应用场景。本质上讲，一个元类会在定义时被触发， 这时候你可以执行一些额外的操作。
#
# 下面是一个例子，利用这个思路来创建类似于 collections 模块中的命名元组的类：
import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super(StructTupleMeta, cls).__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple):
    __metaclass__ = StructTupleMeta
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError("{} arguments required".format(len(cls._fields)))
        return super(cls).__new__(StructTuple, args)
