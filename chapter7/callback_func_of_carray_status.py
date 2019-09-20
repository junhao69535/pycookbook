#!coding=utf-8

"""
    带额外状态信息的回调函数
"""


# 你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)，
# 并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。

# 这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用——特别是跟异步
# 处理有关的。 为了演示与测试，我们先定义如下一个需要调用回调函数的函数：
def apply_async(func, args, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print 'Got: {}'.format(result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)

# 注意到 print_result() 函数仅仅只接受一个参数 result 。不能再传入其他信息。
# 而当你想让回调函数访问其他变量或者特定环境的变量值的时候就会遇到麻烦。


# 为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数。
# 比如，下面这个类会保存一个内部序列号，每次接收到一个 result 的时候序列号加1：
class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print '[{}] Got: {}'.format(self.sequence, result)


r = ResultHandler()
apply_async(add, (2, 3), r.handler)


# 也可以使用闭包
def make_handler():
    sequence = [0]  # python2中闭包不能修改外部函数的变量，只能访问，但如果它是可变类型，可以修改其内部的置，而不是修改该对象

    def handler(result):
        sequence[0] += 1
        print '[{}] Got: {}'.format(sequence[0], result)
    return handler


handler = make_handler()
apply_async(add, (2, 3), handler)
apply_async(add, (4, 5), handler)


# 更高级的用法是协程
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print '[{}] Got: {}'.format(sequence, result)


handler = make_handler()
next(handler)  # 先激活协程
apply_async(add, (2, 3), handler.send)
apply_async(add, (4, 5), handler.send)

