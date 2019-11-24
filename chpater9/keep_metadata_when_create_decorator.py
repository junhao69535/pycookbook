#!coding=utf-8

"""
    创建装饰器时保留函数元信息
"""

# 你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、
# 文档字符串、注解和参数签名都丢失了。

# 任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数。例如：
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print "{}, {}".format(func.__name__, end - start)
        return result
    return wrapper


# 下面我们使用这个被包装后的函数并检查它的元信息：
@timethis
def countdown(n):
    """Counts down"""
    while n > 0:
        n -= 1


countdown(100000)
print countdown.__name__  # countdown
print countdown.__doc__  # Counts down
# 如果忽略了@wraps装饰则
# print countdown.__name__  # wrapper
# print countdown.__doc__  # None

