#!coding=utf-8

"""
    顺序迭代合并后的排序迭代对象
"""


# 有一系列对象，想将它们合并后得到一个排序序列且在上面迭代遍历
# heapq.merge()就可以解决这个问题
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print c


# heapq.merge 可迭代特性意味着它不会立马读取所有序列,返回的是生成器
# heapq.merge() 需要所有输入序列必须是排过序的。