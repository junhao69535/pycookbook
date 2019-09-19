#!coding=utf-8

"""
    文件路径名的操作
"""


# 需要使用路径名获取文件名、目录名和绝对路径等
# 使用os.path模块中的函数来操作路径名
import os
path = r'D:\python\pycookbook\chapter5\test.txt'
print os.path.basename(path)  # 获取路径最后的内容
print os.path.dirname(path)  # 获取路径名
print os.path.join('tmp', 'data', os.path.basename(path))  # 将字符串以路径形式结合
# 扩展用户目录
path = r'~\Data\data.csv'
print os.path.expanduser(path)
# 分开文件扩展，获取文件后缀
print os.path.splitext(path)


# 对于任何的文件名的操作，你都应该使用 os.path 模块
