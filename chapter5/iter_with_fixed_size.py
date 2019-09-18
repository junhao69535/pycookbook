#!coding=utf-8


"""
    固定大小记录的文件迭代
"""


# 想在一个古典给长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代
# 可以使用iter和functools.partial()函数
from functools import partial
RECORD_SIZE = 32
with open('test1.txt', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print r


# 上面的例子中的文件时以二进制模式打开的。 如果是读取固定大小的记录，这通常
# 是最普遍的情况。 而对于文本文件，一行一行的读取(默认的迭代行为)更普遍点。


# partial，偏函数，就是把函数的某几个参数固定下来变成一个函数，如
def getname(name):
    print name


p = partial(getname, 'haha')
# 那么调用p()，就等同于调用getname('haha')