#!coding=utf-8

"""
    以指定列宽格式化字符串
"""

# 有一些长字符串，想以指定的列宽将它们重新格式化。
# 使用textwrap模块来格式化字符串的输出
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print textwrap.fill(s, 70)  # 列宽为79

print textwrap.fill(s, 40)

print textwrap.fill(s, 40, initial_indent='    ')  # 开始缩进4个空格

print textwrap.fill(s, 40, subsequent_indent='    ')  # 除第一行外都缩进4个空格

# textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端大小的时候。
# 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。
# 这个函数只能在python3使用，且开启了终端
# import os
# print os.get_terminal_size().columns