#!coding=utf-8

"""
    反向迭代
"""


# 想反方向迭代一个序列
# 可以使用内置的reversed()函数
a = [1, 2, 3, 4]
for x in reversed(a):
    print x


# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__()
# 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行，
with open('passwd.txt') as f:
    for line in reversed(list(f)):
        print line,


# 要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存。

# 可以通过实现__reversed__()来实现反向迭代
class Countdown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print rr
for rr in Countdown(30):
    print rr


# 定义一个反向迭代器可以使得代码非常的高效， 因为它不再需要将数据填充到
# 一个列表中然后再去反向迭代这个列表。