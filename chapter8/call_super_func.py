#!coding=utf-8

"""
    调用父类方法
"""


# 想调用父类某个已经被重写的方法
class A(object):
    def spam(self):
        print 'A.spam'


class B(A):
    def spam(self):
        print 'B.spam'
        super(B, self).spam()  # 在python3里是super().spam()，根据mro调用


B().spam()


class Base(object):
    def __init__(self):
        print 'Base.__init__'


class C(Base):
    def __init__(self):
        super(C, self).__init__()
        print 'C.__init__'


class D(Base):
    def __init__(self):
        super(D, self).__init__()
        print 'D.__init__'


class E(C, D):
    def __init__(self):
        super(E, self).__init__()
        print 'E.__init__'


# E是多继承，调用super()时的调用顺序是按照mro进行的，python2中只有新式类采用mro，而且
# mro不是在类dict中，而是作为类方法提供
# [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.Base'>, <type 'object'>]
print E.mro()
E()  # 结果和mro有关


# MRO的构造是通过一线C3线性化算法实现，有三条准则：
# 1、子类会先于父类被检查
# 2、多个父类会根据它们在列表中的顺序被检查
# 3、如果对下一个类存在两个合法的选择，选择第一个父类


# super() 有个令人吃惊的地方是它并不一定去查找某个类在MRO中下一个直接父类， 你甚至
# 可以在一个没有直接父类的类中使用它，这仅支持python3
class A(object):
    def spam(self):
        print 'A.spam'
        super(A, self).__init__()


class B(object):
    def spam(self):
        print 'B.spam'


class C(A, B):
    pass


C().spam()  # A.spam   B.spam
# 在定义混入类的时候这样使用 super() 是很普遍的。
