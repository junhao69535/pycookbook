#!coding=utf-8

"""
    定义接口或者抽象基类
"""


# 定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法
from abc import ABCMeta, abstractmethod


class IStream(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 抽象类不能直接被实例化
# 抽象类的目的就是让别的类继承它并实现特定的抽象方法
# 如果继承的类没有实现所有的抽象方法，则它仍然是一个抽象类
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# 抽象基类的一个主要用途是在代码中检查某些类是否特定类型，实现了特定接口：
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


# 除了继承，也可以通过注册方式让某个类实现抽象基类
import io

IStream.register(io.IOBase)

f = open('foo.txt')
isinstance(f, IStream)

# 尽管ABCs可以让我们很方便的做类型检查，但是我们在代码中最好不要过多的使用它。
# 因为Python的本质是一门动态编程语言，其目的就是给你更多灵活性， 强制类型检查
# 或让你代码变得更复杂，这样做无异于舍本求末。