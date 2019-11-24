#!coding=utf-8
"""
    将装饰器定义为类
"""

# 你想使用一个装饰器去包装函数，但是希望返回一个可调用的实例。 你需要让你的装饰器可以同时工作在
# 类定义的内部和外部。
import types
from functools import wraps


class Profiled(object):
    def __init__(self, func):
        self._ori_func = func
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        # return self.__wrapped__(*args, **kwargs)  # 调用原函数，仅支持python3
        return self._ori_func(*args, **kwargs)

    def __get__(self, instance, cls):  # 实际上就是一个描述器
        if instance is None:
            # 当直接用类调用方法，这个判断会触发，如Spam.bar
            return self
        else:
            return types.MethodType(self, instance)  # 把实例绑定到self


# 你可以将它当做一个普通的装饰器来使用，在类里面或外面都可以：
@Profiled
def add(x, y):
    return x + y


class Spam(object):
    @Profiled  # 使用了这个装饰器后，返回的是Profiled对象，而不是Spam对象，因此Profiled定义的__get__()方法很重要
    def bar(self, x):
        print "{}, {}".format(self, x)
    # @Profiled就是描述器，因此当调用bar时会调用描述器的__get__()方法


# 将装饰器定义成类通常是很简单的。但是这里还是有一些细节需要解释下，特别是当你想将它作用在
# 实例方法上的时候。
#
# 首先，使用 functools.wraps() 函数的作用跟之前还是一样，将被包装函数的元信息复制到可调用实例中去。
#
# 其次，通常很容易会忽视上面的 __get__() 方法。如果你忽略它，保持其他代码不变再次运行， 你会
# 发现当你去调用被装饰实例方法时出现很奇怪的问题。例如：
# s = Spam()  # 在没有__get__()的情况下测试
# s.bar(5)  # TypeError: bar() takes exactly 2 arguments (1 given)
# 当调用s.bar返回的是Profiled的对象，然后

# 出错原因是当方法函数在一个类中被查找时，它们的 __get__() 方法依据描述器协议被调用，
# 在8.9小节已经讲述过描述器协议了。在这里，__get__() 的目的是创建一个绑定方法对象
# (最终会给这个方法传递self参数)。下面是一个例子来演示底层原理：
# s = Spam()
# def grok(self, x):
#     pass


# print grok.__get__(s, Spam)  # <bound method Spam.grok of <__main__.Spam object at 0x000000000356FB70>>
# __get__() 方法是为了确保绑定方法对象能被正确的创建。 type.MethodType() 手动创建
# 一个绑定方法来使用。只有当实例被使用的时候绑定方法才会被创建。 如果这个方法是在
# 类上面来访问， 那么 __get__() 中的instance参数会被设置成None并直接返回
# Profiled 实例本身。 这样的话我们就可以提取它的 ncalls 属性了。