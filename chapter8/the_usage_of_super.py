#!coding=utf-8

"""
    super的用法
"""


class A(object):
    def __init__(self):
        self.a = 'A'

    def print_a(self):
        print 'In A'
        print self.a


class B(A):
    def __init__(self):
        pass

    def print_a(self):
        print 'In B'
        print self.a


# b = B()
# b.print_a()  # error

# 强调一点：super不是python关键字，而是内建类，是语法糖。

class A(object):
    def __init__(self):
        super(A, self).__init__()
        self.a = 'A'

    def print_a(self):
        print 'In A'
        print self.a


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def print_a(self):
        print 'In B'
        print self.a


b = B()
b.print_a()
print B.__mro__