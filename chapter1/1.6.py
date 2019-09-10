#!coding=utf-8

"""
    字典中的键映射多个值
"""

# 实现一个键对应多个值的字典（也叫multidict）
# 只要把多个值放在另外的容器即可，如：
# 如果要保持插入顺序，可以使用列表
d1 = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
# 如果要去重复，可以使用集合
d2 = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


# 可以collections模块中的defaultdict来构造，它的特征是会自动初始化每个key刚开始对应的值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print d

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print e

# 需要注意的是， defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射
# 实体。如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：
f = {}  # 一个普通的字典
f.setdefault('a', []).append(1)
f.setdefault('a', []).append(2)
f.setdefault('b', []).append(4)
print f