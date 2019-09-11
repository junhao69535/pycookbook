#!coding=utf-8

"""
    查找两字典的相同点
"""

# 在两字典中寻找相同点（如相同的键，相同的值）
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 可以使用keys()和items()方法返回的结果执行集合操作
# python2不支持，因为python2中dict.keys()返回的是list，而python3返回的是dict_keys
# 同理，dict.items()也不能这样操作。
# print a.keys() & b.keys()
# print a.keys() - b.keys()
# print a.items() & b.items()