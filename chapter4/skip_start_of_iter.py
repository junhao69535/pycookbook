#!coding=utf-8

"""
    跳过可迭代对象的开始部分
"""


# itertools 模块中有一些函数可以完成这个任务。 首先介绍的是 itertools.dropwhile()
# 函数。使用时，你给它传递一个函数对象和一个可迭代对象。 它会返回一个迭代器对象，
# 丢弃原有序列中直到函数返回Flase之前的所有元素，然后返回后面所有元素。
from itertools import dropwhile
with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print line,


# 这个例子是基于根据某个测试函数跳过开始的元素。 如果你已经明确知道了要跳过的元素
# 的个数的话，那么可以使用 itertools.islice() 来代替。比如：
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print x
