#!coding=utf-8

"""
    通过某个字段将记录分组
"""

# 有一个字典或者实例的序列，需要根据某个特定字段如date来分组迭代访问

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))  # 必须先排序，否则分组实拍
for date, items in groupby(rows, key=itemgetter('date')):
    print date
    for i in items:
        print ' ', i


# groupby()扫描整个序列并且查询连续相同值的元素序列，这就是要先排序的原因。
# 每次迭代都会返回一个值和一个迭代器对象。


# 如果只是想根据date字段将数据分组到一个大的数据结构中去，并且允许随机访问，
# 最好使用defaultdict()。
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)