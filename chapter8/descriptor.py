#!coding=utf-8

"""
    创建新的类或实例属性
"""


# 创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。
# 如果你想创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功能。
class Interger(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print instance, cls
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):  # 没有cls，不支持改变描述器
        if not isinstance(value, int):
            raise TypeError('Excepted an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# 一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类， 分别
# 为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。 这些方法接受一个
# 实例作为输入，之后相应的操作实例底层的字典。
class Point(object):
    x = Interger('x')
    y = Interger('y')

    def __init__(self, x, y, z):
        self.x = x  # 会调用描述器的__set__()方法
        self.y = y
        self.z = z  # 调用默认的描述器的__set__()方法


# 当你这样做后，所有对描述器属性(比如x或y)的访问会被 __get__() 、__set__() 和
# __delete__() 方法捕获到。例如：
p = Point(3, 4, 5)
print p.x  # 会调用描述器的__get__()方法，instance是这个p对象，cls是这个Point类
p.y = 5  # 会调用描述器的__set__()方法
print Point.__dict__
print p.__dict__
# 当用类去访问描述器时，instance是None，class是这个Point类，这种情况下，标准做法
# 就是简单的返回这个描述器本身即可(尽管你还可以添加其他的自定义操作)，如下：
print Point.x  # 返回了这个描述器本身

# 描述器可实现大部分Python类特性中的底层魔法， 包括 @classmethod 、@staticmethod 、
# @property ，甚至是 __slots__ 特性。

# 通过定义一个描述器，你可以在底层捕获核心的实例操作(get, set, delete)，并且可完全
# 自定义它们的行为。 这是一个强大的工具，有了它你可以实现很多高级功能，并且它也是很多
# 高级库和框架中的重要工具之一。


# 描述器通常是那些使用到装饰器或元类的大型框架中的一个组件。同时它们的使用也被隐藏在后面。
class Typed(object):
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Excepted {}'.format(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


@typeassert(name=str, shares=int, prince=float)
class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

# 最后要指出的一点是，如果你只是想简单的自定义某个类的单个属性访问的话就不用去写描述器了
# 。 这种情况下使用8.6小节介绍的property技术会更加容易。 当程序中有很多重复代码的时候
# 描述器就很有用了 (比如你想在你代码的很多地方使用描述器提供的功能或者将它作为一个函数
# 库特性)。