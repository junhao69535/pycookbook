#!coding=utf-8

"""
    带可选参数的装饰器
"""


# 你想写一个装饰器，既可以不传参数给它，比如 @decorator ， 也可以传递
# 可选参数给它，比如 @decorator(x,y,z) 。
from functools import wraps, partial
import logging


def logged(func=None, level=logging.DEBUG, name=None, message=None):
    # 全部使用默认参数，且必须有func这个参数。当直接@logged，则相当于最简单的装饰器
    # 如add这个例子，这就是把add最为func参数传进来。而spam这个例子，首先不提供func，
    # 返回一个偏函数，仍然作为装饰器，然后传进spam作为func参数。
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__name__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name="example")
def spam():
    print "Spam!"