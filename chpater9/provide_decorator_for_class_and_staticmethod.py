#!coding=utf-8
"""
    为类和静态方法提供装饰器
"""

# 给类或静态方法提供装饰器是很简单的，不过要确保装饰器在 @classmethod 或 @staticmethod 之前。例如：
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print end - start
        return r
    return wrapper


class Spam(object):
    @timethis
    def instance_method(self, n):
        print self, n
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print cls, n
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print n
        while n > 0:
            n -= 1


# class Spam:
#     @timethis
#     @staticmethod
#     def static_method(n):
#         print(n)
#         while n > 0:
#             n -= 1
# 着用会报错
# 问题在于 @classmethod 和 @staticmethod 实际上并不会创建可直接调用的对象， 而是创
# 建特殊的描述器对象(参考8.9小节)。因此当你试着在其他装饰器中将它们当做函数来
# 使用时就会出错。 确保这种装饰器出现在装饰器链中的第一个位置可以修复这个问题。