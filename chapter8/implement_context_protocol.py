#!coding=utf-8

"""
    让对象支持上下文管理协议
"""


# 为了让一个对象兼容with语句，需要实现__enter__()和__exit__()方法：
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()  # 这样写的话，with语句只能嵌套


from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send('GET /index.html HTTP/1.0\r\n')
    s.send('Host: www.python.org\r\n')
    s.send('\r\n')
    resp = ''.join(iter(partial(s.recv, 8192), ''))
    print resp


# 编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。 当出现 with 语句
# 的时候，对象的 __enter__() 方法被触发， 它返回的值(如果有的话)会被赋值给 as 声明
# 的变量。然后，with 语句块里面的代码开始执行。 最后，__exit__() 方法被触发进行清理工作。

# 不管 with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是一样的。
# 事实上，__exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息(如果有的话)。
# __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个None值。
# 如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生一样，
# with 语句后面的程序继续在正常执行。

