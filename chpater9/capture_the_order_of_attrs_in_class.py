#!coding=utf-8
"""
    捕获类的属性定义顺序
"""

# 你想自动记录一个类中属性和方法定义的顺序， 然后可以利用它来做很多操作（比如序列化、映射到数据库等等）。
# 利用元类可以很容易的捕获类的定义信息。下面是一个例子，使用了一个OrderedDict来记录描述器的定义顺序：
from collections import OrderedDict


# 各种类型的描述器
class Typed(object):
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError("Expected {}".format(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


# 使用OrderDict的元类
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d["_order"] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        # 这个方法仅支持python3
        print "im a prepare"
        return OrderedDict()


# 下面是一个简单的类，使用这个排序字典来实现将一个类实例的数据序列化为一行CSV数据：
class Structure(object):
    __metaclass__ = OrderedMeta

    def as_csv(self):
        return ",".join(str(getattr(self, name)) for name in self._order)


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock("GOOD", 100, 490.1)
print s.name
print s.as_csv()

# 本节一个关键点就是OrderedMeta元类中定义的 `` __prepare__()`` 方法。 这个方法会在
# 开始定义类和它的父类的时候被执行。它必须返回一个映射对象以便在类定义体中被使用到。
# 我们这里通过返回了一个OrderedDict而不是一个普通的字典，可以很容易的捕获定义的顺序。