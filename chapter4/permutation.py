#!coding=utf-8

"""
    排列组合的迭代
"""

# 像迭代遍历一个集合中元素的所有可能的排列或组合
# itertools模块提供了三个函数来解决这类问题,其中一个是 itertools.permutations() ，
# 它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。
from itertools import permutations  # 排列
items = ['a', 'b', 'c']
for p in permutations(items):  # A33
    print p


# 如果想得到指定长度的所有排列，可以：
for p in permutations(items, 2):  # A32
    print p


from itertools import combinations  # 组合
for c in combinations(items, 3):  # C33
    print c

for c in combinations(items, 2):  # C32
    print c

for c in combinations(items, 1):  # C31
    print c


# 在计算组合的时候，一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取了，
# 那么接下来就不会再考虑它了)。 而函数 itertools.combinations_with_replacement()
# 允许同一个元素被选择多次，比如：
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print c