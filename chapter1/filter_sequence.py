#!coding=utf-8

"""
    过滤序列元素
"""

# 有一个数据序列，想利用规则提取出需要的值或者缩短序列
# 最简单的是列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print [n for n in mylist if n > 0]
print [n for n in mylist if n < 0]

# 当输入非常大，使用列表推导会产生一个非常大结果，占用大量内存。可以使用
# 生成器改善性能。
pos = (n for n in mylist if n > 0)
for p in pos:
    print p,
print


# 有时候，过滤规则比较复杂，不能简单使用列表推导或者生成器表达式。要处理复杂
# 的过滤，先把过滤内容放到函数，再调用内置filter()函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = filter(is_int, values)
print ivals


# 另外一个值得关注的过滤工具就是 itertools.compress() ， 它以一个 iterable 对象
# 和一个相对应的 Boolean 选择器序列作为输入参数。 然后输出 iterable 对象中对应
# 选择器为 True 的元素。 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个
# 函数是非常有用的。 比如，假如现在你有下面两列数据：
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print more5
print list(compress(addresses, more5))

# 和filter()一样，compress()返回的也是一个迭代器