#!coding=utf-8

"""
    字节字符串上的字符串操作
"""

# 想在字节字符串上执行普通的文本操作（比如移除，搜索和替换）。
# 字节字符串同样支持大部分和文本字符串一样的内置操作。
data = 'Hello World'  # 在python2，str就是字节字符串，不需要加b
print data[0:5]
print data.startswith('Hello')
print data.split()
print data.replace('Hello', 'Hello Cruel')

# 这些操作同样也适用于字节数组
data = bytearray('Hello World')
print data[0:5]
print data.startswith('Hello')
print data.split()
print data.replace('Hello', 'Hello Cruel')

# 如果使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节字符串
# 这个约束在python2中不适用
data = 'FOO:BAR,SPAM'
import re
print re.split('[:,]', data)


# 字节字符串的索引操作返回整数而不是单独字符
# 但在python2中不适用于字节字符串，只适用于bytearray
a = 'Hello World'
print a[0]
b = bytearray('Hello World')
print b[0]  # 默认ascii编码


# 注：处理文本字符串没有必要为了性能能改用字节字符串来操作。