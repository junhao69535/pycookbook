#!coding=utf-8

"""
    字符串开头或结尾匹配
"""

# 需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等
# 最简单的是使用str.startswith()和str.endswith()
filename = 'spam.txt'
print filename.endswith('.txt')
print filename.startswith('file:')
url = 'http://python.org'
print url.startswith('http:')


# 如果想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中（必须是元组），然后
# 传给startswith()和endswith()方法：
import os
filenames = os.listdir('.')
print filenames

print [name for name in filenames if name.endswith(('.h', '.py'))]


# 最后提一下，当和其他操作比如普通数据聚合相结合的时候 startswith() 和 endswith() 方法
# 是很不错的。 比如，下面这个语句检查某个文件夹中是否存在指定的文件类型
# if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):