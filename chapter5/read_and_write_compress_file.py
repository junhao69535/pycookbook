#!coding=utf-8

"""
    读写压缩文件
"""


# 想读写一个gzip或者bz2格式的文件
# 可以使用gzip和bz2模块处理，gzip有open()函数，bz2需要使用别的方法处理
import gzip
with gzip.open('test.gz', mode='r') as f:
    text = f.read()
    print text


import bz2
f1 = bz2.BZ2File('a.txt.bz2')
print f1.read()


# 写入内容
# 默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低。
with gzip.open('test.gz', mode='a', compresslevel=9) as f:
    f.write('this is a test!')

f2 = bz2.BZ2File('a.txt.bz2', mode='w', compresslevel=9)  # 不支持追加
f2.write('this is a test')

# 最后一点， gzip.open() 和 bz2.open() 还有一个很少被知道的特性， 它们
# 可以作用在一个已存在并以二进制模式打开的文件上。比如，下面代码是可行的：
# f = open('test.gz', 'rb')
# with gzip.open(f, 'r') as g:
#     text = g.read()
#     print text

# 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，管道和
# 内存中文件等。但这仅适用于python3