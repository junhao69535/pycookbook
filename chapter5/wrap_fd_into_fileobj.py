#!coding=utf-8

"""
    将文件描述符包装成文件对象
"""


# 你有一个对应于操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件
# 描述符， 你想将它包装成一个更高层的Python文件对象。
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'w')
f.write('hello world\n')
f.close()