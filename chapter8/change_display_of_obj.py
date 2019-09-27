#!coding=utf-8

"""
    改变对象的字符串显示
"""


# 想改变一个实例的字符串表示，可重新定义它的__str__()和__repr__()方法
class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# __repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。 内置的
# repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。 __str__()
# 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串。
p = Pair(3, 4)
print repr(p)
print p


# 我们在这里还演示了在格式化的时候怎样使用不同的字符串表现形式。 特别来讲，!r 格式化代码
# 指明输出使用 __repr__() 来代替默认的 __str__()
p = Pair(3, 4)
print 'p is {0!r}'.format(p)
print 'p is {0}'.format(p)