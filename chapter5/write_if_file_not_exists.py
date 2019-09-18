#!coding=utf-8

"""
    文件不存在才能写入
"""


# 想先测试文件是否存在再写入，避免覆盖已存在的文件内容
# 指定模式为'x'，但仅支持python3
# with open('test1.txt', 'x') as f:
#     f.write('测试！')


# python2只能利用os
import os
path = os.getcwd()
filename = os.path.join(path, 'test1.txt')
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write('测试！')
else:
    print('file already exists!')