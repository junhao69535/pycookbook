#!coding=utf-8
"""
    创建缓存实例
"""

# 在创建一个类的对象时，如果之前使用同样参数创建过这个对象， 你想返回它的缓存引用。

# 这种通常是因为你希望相同参数创建的对象时单例的。 在很多库中都有实际的例子，
# 比如 logging 模块，使用相同的名称创建的 logger 实例永远只有一个。
import logging
a = logging.getLogger("foo")
b = logging.getLogger("bar")
print a is b  # False
c = logging.getLogger("foo")
print a is c  # True


# 为了达到这样的效果，你需要使用一个和类本身分开的工厂函数，例如：
class Spam(object):
    def __init__(self, name):
        self.name = name


# 支持缓存
import weakref


_spam_cache = weakref.WeakValueDictionary()  # 保存的是对象的弱引用，当对象被删除，该字典也不存在这个对象的引用了
def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


a = get_spam("foo")
b = get_spam("bar")
print a is b  # False
c = get_spam("foo")
print a is c  # True


# 当我们保持实例缓存时，你可能只想在程序中使用到它们时才保存。 一个 WeakValueDictionary
# 实例只会保存那些在其它地方还在被使用的实例。 否则的话，只要实例不再被使用了，它就从字典
# 中被移除了。观察下下面的测试结果：
a = get_spam("foo")
b = get_spam("bar")
c = get_spam("foo")
print list(_spam_cache)
del a
del c
print list(_spam_cache)
del b
print list(_spam_cache)


# 对于大部分程序而已，这里代码已经够用了。不过还是有一些更高级的实现值得了解下。
#
# 首先是这里使用到了一个全局变量，并且工厂函数跟类放在一块。我们可以通过将缓存代码放到一个单独的缓存管理器中：
class CachedSpamManager(object):
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()  # 本身不占引用计数

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam(object):
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(self, name):
        return self.manager.get_spam(name)


# 这样的话代码更清晰，并且也更灵活，我们可以增加更多的缓存管理机制，只需要替代manager即可。
# 还有一点就是，我们暴露了类的实例化给用户，用户很容易去直接实例化这个类，而不是使用工厂方法，如
a = Spam("foo")
b = Spam("foo")
print a is b


# 有几种方式可以防止用户这样做，第一个是将类的名字修改为以下划线(_)开头，提示用户别直接调用它。
# 第二种就是让这个类的 __init__() 方法抛出一个异常，让它不能被初始化：
class Spam(object):
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


# 然后修改缓存管理器代码，使用 Spam._new() 来创建实例，而不是直接调用 Spam() 构造函数：
class CachedSpamManager2(object):
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam3(object):
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self