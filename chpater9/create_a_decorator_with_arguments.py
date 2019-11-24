#!coding=utf-8

"""
    定义一个带参数的装饰器
"""
from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# 示例
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print "Spam!"


# 初看起来，这种实现看上去很复杂，但是核心思想很简单。 最外层的函数 logged() 接受参数
# 并将它们作用在内部的装饰器函数上面。 内层的函数 decorate() 接受一个函数作为参数，
# 然后在函数上面放置一个包装器。 这里的关键点是包装器是可以使用传递给 logged() 的参数的。