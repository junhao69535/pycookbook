#!coding=utf-8

"""
    命名切片
"""

# 如果程序包含了大量无法直视的硬编码切片，需要清理代码
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])


# 与其这样写，不如这样命名切片
SHARES = slice(20, 23)
PRICES = slice(31, 37)
print int(record[SHARES]) * float(record[PRICES])


# 内置的slice()创建一个切片对象，所有使用切片的地方都可以使用切片对象
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print items[2:4], items[a]


# 切片对象的start,stop,step属性可以获取其信息
a = slice(5, 50, 2)
print a.start, a.stop, a.step


# 除此之外，还用调用indices(size)方法将切片映射到一个已知大小的序列上。这个方法
# 返回一个三元组(start, stop, step)，所有的值都会被缩小，直到适合这个已知序列的
# 边界为止。这样，不会抛出IndexError异常
s = 'HelloWorld!'
print a.indices(len(s))
for i in range(*a.indices(len(s))):
    print s[i]