#!coding=utf-8

"""
    在函数上添加包装器
"""

# 你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)。
# 如果你想使用额外的代码包装一个函数，可以定义一个装饰器函数，例如：
import time
from functools import wraps


def timethis(func):
    """
    用于统计时间
    """
    @wraps(func)
    def warpper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print "{}, {}".format(func.__name__, end - start)
        return result
    return warpper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(100000)

# 比如上面使用 @wraps(func) 注解是很重要的， 它能保留原始函数的元数据