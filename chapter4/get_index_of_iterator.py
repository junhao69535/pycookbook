#!coding=utf-8

"""
    序列上索引值迭代
"""


# 想在迭代一个序列的同时跟踪正在被处理的元素索引。
# 内置的enumberate()函数可以很好解决
my_list = ['a', 'b', 'c']
for ind, val in enumerate(my_list, 1):  # 指定从1开始，默认从0开始
    print ind, val


# 迭代文件内容时可以得到行号，更容易排除问题