#!coding=utf-8

"""
    增加或改变已打开文件的编码
"""


# 想在不关闭已打开的文件前提下增加或改变它的Unicode编码
# 如果想给一个以二进制模式打开的文件添加Unicode编码/解码方式，可以使用
# io.TextIOWrapper()对象包装它
import urllib2
import io

# 在python2下有点问题
# u = urllib2.urlopen('http://www.python.org')
# print dir(u)
# f = io.TextIOWrapper(u, encoding='utf-8')
# print f.read()


# 如果你想修改一个已经打开的文本模式的文件的编码方式，可以先使用 detach() 方法
# 移除掉已存在的文本编码层， 并使用新的编码方式代替。
# 也仅支持python3
# import sys
# print sys.stdout.encoding
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
# print sys.stdout.encoding


# I/O系统由一系列的层次构建而成。你可以试着运行下面这个操作一个文本文件的例子
# 来查看这种层次
# f = open('sample.txt', 'w')
# print type(f)
# # print f.buffer
# # print f.buffer.raw
# f.close()


# 这部分内容基本是python3内容，如果使用python3可以看一下，也能理解python的io