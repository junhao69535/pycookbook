#!coding=utf-8

"""
    字符串的I/)操作
"""


# 想操作类文件对象的程序来操作文件操作字符串数据
# 可以使用io.StringIO()和io.BytesIO()类来创建类文件对象操作字符串数据
import io
s = io.StringIO()  # 要求写的是unicode字符串
s.write(u'Hello World!')  # 这实际是写进内存里面，不会写到disk，但s可以作为类文件对象
# print >> s, u'This is a test!'  # 在python下出现问题
print s.getvalue()  # 获取这个类文件对象的内容

# 把字符串包装成一个文件接口
s1 = io.StringIO(u'Hello\nWorld\n')
print s1.read(4)  # 会读取四个字节
print s1.read()  # 会读取剩下的字节


# io.StringIO只能用于文本，如果想操作二进制数据，要使用io.BytesIO
s2 = io.BytesIO()
s2.write('Hello, World')
print s2.getvalue()


# 当你想模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。
# 比如，在单元测试中，你可以使用 StringIO 来创建一个包含测试数据的类文件对象，
# 这个对象可以被传给某个参数为普通文件对象的函数。

# 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。
# 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
