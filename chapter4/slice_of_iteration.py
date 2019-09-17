#!coding=utf-8

"""
    迭代器切片
"""


# 想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
# 函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作。
import itertools
def count(n):
    while True:
        yield n
        n += 1


c = count(0)
for x in itertools.islice(c, 10, 20):
    print x


# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有
# 实现索引)。 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到
# 切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置。