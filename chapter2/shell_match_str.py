#!coding=utf-8

"""
    用Shell通配符匹配字符串
"""

# 想使用Unix Shell中常用的通配符（比如*.py，Dat[0-9]*.csv等）去匹配文本字符串

# fnmatch模块提供了两个函数fnmatch()和fnmatchcase()，可以实现这样的匹配
from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')
print fnmatch('foo.txt', '?oo.txt')
print fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print [name for name in names if fnmatch(name, 'Dat*.csv')]

# fnmatch()大小写敏感取决于底层操作系统
# 如果对于这个区别很在意，可以使用fnmatchcase()来代替
# 这两个函数对字符串操作也是可以的。


# 如果你的代码需要做文件名的匹配，最好使用 glob 模块