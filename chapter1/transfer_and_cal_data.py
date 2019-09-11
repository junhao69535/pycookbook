#!coding=utf-8

"""
    转换并同时计算数据
"""

# 需要在数据序列上执行聚合函数(sum(),min(),max()）等，但是需要先转换或者过滤数据
# 一个优雅的方式是使用生成器表达式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

import os
files = os.listdir('d:\\python\\pycookbook\\chapter1')
if any(name.endswith('.py') for name in files):
    print 'There be python!'
else:
    print 'Sorry, no python.'

s = ('ACME', 50, 123.45)
print ','.join(str(x) for x in s)

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print min_shares

# 在使用一些聚集函数比如 min() 和 max() 的时候你可能更加倾向于使用生成器版本， 它们
# 接受的一个 key 关键字参数或许对你很有帮助。 比如，在上面的证券例子中，你可能会考虑
# 下面的实现版本：
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
print min_shares
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print min_shares