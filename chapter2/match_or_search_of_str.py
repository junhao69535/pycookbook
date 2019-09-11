#!coding=utf-8

"""
    字符串匹配和搜索
"""

# 如果只是想匹配字面字符串，通常只需要调用基本字符串方法即可，如：str.find()，
# str.endswith()和str.startswith()或者类似的方法
text = 'yeah, but no, but yeah, but no, but yeah'
print text == 'yeah'
print text.startswith('yeah')
print text.endswith('yeah')
print text.find('no')


# 对于复杂的匹配需要使用正则表达式。
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
    print 'yes'
else:
    print 'no'

if re.match(r'\d+/\d+/\d+', text2):
    print 'yes'
else:
    print 'no'


# 如果想使用同一个模式去做多次匹配，应该先将模式字符串预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if re.match(datepat, text1):
    print 'yes'
else:
    print 'no'

if re.match(datepat, text2):
    print 'yes'
else:
    print 'no'


# match()总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置，使用
# findall()方法替代
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print datepat.findall(text)


# 在定义正则式的时候，通常会利用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(3)
print m.groups()
month, day, year = m.groups()
print datepat.findall(text)


# match()会返回Match对象，而findall()会返回所有结果
# findall()会搜索文本并以列表形式返回所有的匹配。如果想以迭代方式返回匹配，可以使用
# finditer()替代,finditer()返回的每个元素都是Match对象。
for m in datepat.finditer(text):
    print type(m)
    print m.groups()