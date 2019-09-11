#!coding=utf-8

"""
    删除序列相同元素并保持顺序
"""

# 怎么再一个序列上面保持元素顺序同时消除重复的值
# 如果序列上的值都是hashable类型，直接利用集合和生成器即可
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print list(dedupe(a))


# 如果消除的元素不可哈希，要改成：
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


# 这里key参数指定了一个函数，将序列元素转换成hashable类型
b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print list(dedupe2(b, lambda d: (d['x'], d['y'])))


# 如果仅仅想消除重复元素，不需要保持顺序，直接使用set()即可
print set(a)


# 也可以用于文件消除重复行
with open('somefile.txt') as f:
    for line in dedupe(f):
        print line,