#!coding=utf-8

"""
    减少可调用对象的参数个数
"""


# 有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器，
# 但是它的参数太多了，导致调用时出错。
# 可以使用偏函数，functiools.partial()。
def spam(a, b, c, d):
    print a, b, c, d


from functools import partial
s1 = partial(spam, 1)  # a = 1,把a = 1固定到函数去了
s1(2, 3, 4)
s2 = partial(spam, d=42)  # 把d=42固定到函数去了
s2(1, 2, 3)


# 可以看出 partial() 固定某些参数并返回一个新的callable对象。这个新的
# callable接受未赋值的参数， 然后跟之前已经赋值过的参数合并起来，最后将
# 所有参数传递给原始函数。

# 可以解决的问题是让原来不兼容的代码可以一起工作：
# 假设有一个点的列表来表示(x,y)坐标元组，用以下函数计算两点之间的距离：
import math
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

# 现在假设想以某个点为基点，根据点和基点之间的距离和排序所有这些带你，但
# sort()方法只接受一个关键字参数来自定义排序逻辑，此时偏函数就有用了：
pt = (4, 3)
points.sort(key=partial(distance, pt))
print points


# 更进一步，partial() 通常被用来微调其他库函数所使用的回调函数的参数。
# 例如，下面是一段代码，使用 multiprocessing 来异步计算一个结果值， 然后
# 这个值被传递给一个接受一个result值和一个可选logging参数的回调函数：
# 这个例子只支持unix环境
# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Got: %r', result)
#
#
# def add(x, y):
#     return x + y
#
# import logging
# from multiprocessing import Pool
# from functools import partial
# logging.basicConfig(level=logging.DEBUG)
# log = logging.getLogger('test')
#
# p = Pool()
# p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
# p.close()
# p.join()