#!coding=utf-8


"""
    将装饰器定义为类的一部分
"""

# 你想在类中定义装饰器，并将其作用在其他函数或方法上。

# 在类里面定义装饰器很简单，但是你首先要确认它的使用方式。比如到底是作为一个实例方法还是类方法。
# 下面我们用例子来阐述它们的不同：
from functools import wraps


class A(object):
    # 示例方法作为装饰器
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print "Decorator 1"
            return func(*args, **kwargs)
        return wrapper

    # 类方法作为装饰器
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print "Decorator 2"
            return func(*args, **kwargs)
        return wrapper


# 示例方法
a = A()
@a.decorator1
def spam():
    pass


# 类方法
@A.decorator2
def grok():
    pass


# 仔细观察可以发现一个是实例调用，一个是类调用。

# 在类中定义装饰器初看上去好像很奇怪，但是在标准库中有很多这样的例子。 特别的，@property 装饰器实际
# 上是一个类，它里面定义了三个方法 getter(), setter(), deleter() , 每一个方法都是一个装饰器。例如：
class Person(object):
    # 创建一个property实例
    first_name = property()

    # 应用装饰方法
    # property直接作为装饰器的话，它会以被装饰的函数名创建出一个实例
    @first_name.getter  # 这实际上是一个实例方法，和上面例子的decorator1一样。
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value