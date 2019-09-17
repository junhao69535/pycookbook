#!coding=utf-8

"""
    同时迭代多个序列
"""

# 想同时迭代多个序列，每次分别从一个序列中取一个元素。
# 可以使用zip()函数
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):  # 迭代的长度和最短序列长度一致
    print x, y


# 如果不像迭代的长度和最短序列一致，可以使用itertools.zip_longest()
from itertools import izip_longest
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in izip_longest(a, b, fillvalue=0):  # 默认填充的是Nonne
    print i


# 可以使用zip()打包生成一个字典
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
print s


# 虽然不常见，但是 zip() 可以接受多于两个的序列的参数。 这时候所生成的
# 结果元组中元素个数跟输入序列个数一样。

# 最后强调一点就是， zip() 会创建一个迭代器来作为结果返回。 如果你需要将
# 结对的值存储在列表中，要使用 list() 函数