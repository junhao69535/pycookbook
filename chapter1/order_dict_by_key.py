#!coding=utf-8

"""
    通过某个关键字排序一个字典列表
"""

# 有一个字典列表，想根据某个或某几个字典字段来排序
# 可以使用operator模块的itemgetter()函数
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# 不使用itemgetter()也可以：
# rows_by_fname = sorted(rows, key=lambda d: d['lname'])
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print rows_by_fname
print rows_by_uid


# itemgetter()函数也支持多个keys
rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
print rows_by_lname
# 不使用itemgetter()也可以：
# rows_by_lname = sorted(rows, key=lambda d: (d['lname'], d['fname']))


# 两个方法都可以，但是itemgetter()性能会更好。
# 也使用min()和max()函数
print min(rows, key=itemgetter('uid'))
print max(rows, key=itemgetter('uid'))