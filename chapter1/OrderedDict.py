#!coding=utf-8

"""
    字典排序
"""

# 创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
# 可以使用collections的OrderedDict
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print key, d[key]

# 当想要构建一个将来需要序列化或编码成其他格式的映射的时候，OrderedDict非常有用。
# 比如，想要精确控制JSON编码后字段的顺序。
import json
print json.dumps(d)

# OrderedDict内部维护这一个根据建插入顺序排序的双向链表。每次当一个新的元素进来
# 的时候，它会被放到链表的尾部。对于一个已经存在的键重复赋值不会改变键的顺序。

# 但OrderedDict的大小是普通字典的两倍，因为它内部维护这另外一个链表。因此当构造
# 一个需要大量OrderedDict实例的数据结构，需要考虑性能。