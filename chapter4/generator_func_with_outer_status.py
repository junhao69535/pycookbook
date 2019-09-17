#!coding=utf-8

"""
    带有外部状态的生成器函数
"""


# 想定义一个生成器函数，但它的会调用某个你想暴露给用户使用的外部状态值
# 可以实现一个类，把生成器函数放在__iter__()方法中
from collections import deque


class linehistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('passwd.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print '{}:{}'.format(lineno, hline),


# 关于生成器，很容易掉进函数无所不能的陷阱。 如果生成器函数需要跟你的程序其他部分
# 打交道的话(比如暴露属性值，允许通过方法调用来控制等等)， 可能会导致你的代码异常
# 的复杂。 如果是这种情况的话，可以考虑使用上面介绍的定义类的方式。 在 __iter__()
# 方法中定义你的生成器不会改变你任何的算法逻辑。 由于它是类的一部分，所以允许你定义
# 各种属性和方法来供用户使用。