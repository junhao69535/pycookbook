#!coding=utf-8

"""
    最短匹配模式
"""

# 使用正则表达式匹配的文本，找到都是模式的最长可能匹配，现在需要最短匹配
import re
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print str_pat.findall(text1)
text2 = 'Computer says "no." Phone says "yes."'
print str_pat.findall(text2)


# 默认下正则是贪婪的，为了解决这个问题，需要在'*'操作符后面加'?'
str_pat = re.compile(r'"(.*?)"')
print str_pat.findall(text2)
