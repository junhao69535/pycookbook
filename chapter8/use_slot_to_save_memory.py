#!coding=utf-8

"""
    创建大量对象时节省内存方法
"""


# 程序需要创建大量（可能上百万）的对象， 导致占用很大的内存。
# 对于主要是用来当成简单的数据结构的类而言，你可以通过给类添加 __slots__ 属性
# 来极大的减少实例所占的内存
from pympler import asizeof


class Date(object):
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Date2(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


count1 = 0
for i in xrange(100):
    temp = Date(2012, 1, 12)  # 没有__dict__属性，只有__slots__，类型是list
    # count1 += temp.__sizeof__()
    count1 += asizeof.asizeof(temp)
count2 = 0
for i in xrange(100):
    temp = Date2(2012, 1, 12)  # 存在__dict__属性
    # count2 += temp.__sizeof__()
    count2 += asizeof.asizeof(temp)
print count1
print count2
a = Date(2013, 1, 12)
print a.__slots__
print type(a.__slots__)
b = Date2(2013, 1, 12)
print b.__dict__


# 只有需要大量实例才有用。而且有缺点：
# 1. 每个继承的子类都要重新定义一遍__slots__
# 2. 实例只能包含哪些在__slots__定义的属性，这对写程序的灵活性有影响，比如你由于
# 某个原因新网给instance设置一个新的属性，比如instance.a = 1, 但是由于a不在__slots__
# 里面就直接报错了，你得不断地去修改__slots__或者用其他方法迂回的解决
# 3. 实例不能有弱引用（weakref）目标，否则要记得把__weakref__放进__slots__

# 尽管slots看上去是一个很有用的特性，很多时候你还是得减少对它的使用冲动。 Python的
# 很多特性都依赖于普通的基于字典的实现。 另外，定义了slots后的类不再支持一些普通
# 类特性了，比如多继承。 大多数情况下，你应该只在那些经常被使用到的用作数据结构的
# 类上定义slots (比如在程序中需要创建某个类的几百万个实例对象)。

# 注：不能使用sizeof或sys.getsizeof来判断内存大小，getsizeof只会获取这个类型和
# 对象引用的内存：
# a = [] 64 bytes  a = [3, 4] 80 bytes，没有把3和4这两个整型站得内存算进去。
# Python在sys模块里提供了getsizeof函数，以获取对象的浅层拷贝的内存占用大小。即当
# 你通过这个函数来获取一个数组的内存大小时，它只会返回该数组本身及元素引用（指针）
# 的大小，而不会将元素本身的真实内存大小占用计算进来。

# Python是动态类型语言，Python在存储一个对象时，不仅要存储它的值，还要存储其
# 引用计数和数据类型（引用）等信息，因此，Python对象的内存占用就比C/C++语言多得多。
print Date(2012, 1, 12).__sizeof__()
print asizeof.asizeof(Date(2012, 1, 12))
print Date2(2012, 1, 12).__sizeof__()
print asizeof.asizeof(Date2(2012, 1, 12))