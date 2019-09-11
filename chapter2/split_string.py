#!coding=utf-8

"""
    使用多个界定符分割字符串
"""

# 需要将一个字符串分割为多个字段，但是分隔符（可以周围的空格）并不是固定的

# string对象的split()只适用非常简单的字符串分割情况，它并不允许有多个分隔符或者分隔符周围
# 不确定的空格，这时需要re.split()
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print re.split(r'[;,\s]\s*', line)  # \s表示空格


# 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。
# 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
fields = re.split(r'(;|,|\s)\s*', line)
print fields


# 获取分割字符在某些情况下也是有用的，比如想保留分割字符串，用来在后面重新构造一个
# 新的输出字符串
values = fields[::2]
delimiters = fields[1::2] + ['']
print values
print delimiters

# 使用相同的分隔符重新构造line
print ''.join(v+d for v, d in zip(values, delimiters))


# 如果不像保留分割字符串，但仍想用括号来分组，确定你的分组事非捕获分组，如(?:...)
print re.split(r'(?:,|;|\s)\s*', line)