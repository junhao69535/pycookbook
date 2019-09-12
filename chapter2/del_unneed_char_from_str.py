#!coding=utf-8

"""
    删除字符串中不需要的字符
"""

# 想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白
# strip()方法用于删除开始和结尾的字符。lstrip()和rstrip()分别从左和从右执行
# 删除操作。默认情况下，这下方法会删除空白字符，但也可以指定
s = ' hello world \n'
print s.strip()  # 'hello world' 会把换行符也删掉
print s.lstrip()  # 'hello world \n'
print s.rstrip()  # ' hello world'

t = '-----hello====='
print t.lstrip('-')
print t.strip('-=')

# 这些 strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的
# 但是需要注意的是去除操作不会对字符串的中间的文本产生任何影响。
# 如果你想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法或者是用正则表达式替换。
# 对于更高阶的strip，你可能需要使用 translate() 方法。
