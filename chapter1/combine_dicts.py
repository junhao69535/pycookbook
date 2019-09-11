#!coding=utf-8

"""
    合并多个字典或映射
"""

# 现在有多个字典或者映射，想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找
# 值或者检查某些键是否存在
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 现在想从两个字典中执行查询，先从a找，如果找不到，再到b找
# 这个在python2不支持
from collections import ChainMap
c = ChainMap(a, b)
print c['x']  # from a
print c['y']  # from b
print c['z']  # from a