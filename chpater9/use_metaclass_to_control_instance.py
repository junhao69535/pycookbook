#!coding=utf-8
"""
    使用元类控制实例的创建
"""

# 你想通过改变实例创建方式来实现单例、缓存或其他类似的特性。
# Python程序员都知道，如果你定义了一个类，就能像函数一样的调用它来创建实例，
# 如果你想自定义这个步骤，你可以定义一个元类并自己实现 __call__() 方法。
# 为了演示，假设你不想任何人创建这个类的实例：


class NoInstances(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(object):
    __metaclass__ = NoInstances

    @staticmethod
    def grok(x):
        print "Spam grok"


# 这样的话，用户只能调用这个类的静态方法，而不能使用通常的方法来创建它的实例。例如：
Spam.grok(42)
# s = Spam()  # 会抛出TypeError异常


# 现在，假如你想实现单例模式（只能创建唯一实例的类），实现起来也很简单：
class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super(Singleton, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(object):
    __metaclass__ = Singleton

    def __init__(self):
        print "Creating Spam"


a = Spam()  # 第一次会调用__init__()，打印Creating Spam
b = Spam()  # 第二次不会调用__init__()，不会打印Creating Spam，而是直接返回单例
print a is b  # True


# 最后，假设你想创建8.25小节中那样的缓存实例。下面我们可以通过元类来实现：
import weakref


class Cached(type):
    def __init__(cls, *args, **kwargs):
        super(Cached, cls).__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            obj = super(Cached, cls).__call__(*args, **kwargs)
            cls.__cache[args] = obj
            return obj


class Spam(object):
    __metaclass__ = Cached

    def __init__(self, name):
        print "Creating Spam({!r})".format(name)
        self.name = name


a = Spam("Guido")
b = Spam("Diana")
c = Spam("Guido")  # Cached
print a is b  # False
print a is c  # True


# 利用元类实现多种实例创建模式通常要比不使用元类的方式优雅得多。
#
# 假设你不使用元类，你可能需要将类隐藏在某些工厂函数后面。 比如为了实现一个单例，你你可能会像下面这样写：
class _Spam(object):
    def __init__(self):
        print "Creating Spam"


_spam_instance = None


def Spam():
    global _spam_instance

    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance
    

# 尽管使用元类可能会涉及到比较高级点的技术，但是它的代码看起来会更加简洁舒服，而且也更加直观。