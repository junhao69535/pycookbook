#!coding=utf-8

"""
    在字符串中处理html和xml
"""

# 如果想将HTML或者XML实体如&entity;或&#code替换为对应的文本。再者，需要转换文本中
# 特定的字符（比如<,>,或&)。

# 如果想替换文本字符串中的'<'或者’<'，使用html.escape()函数即可
# s = 'Elements are written as "<tag>text</tag>".'
# # html库在python3才有
# import html
# print html.escape(s)
# # 保持引用，即保持里面的双引号""
# print html.escape(s, quote=False)


# 如果正在处理的是ASCII文本，并且想将非ASCII文本对应的比那吗实体嵌入进去，可以给某些
# I/O函数传递参数errors='xmlcharrefreplace'来达到目的
s = u'Spicy Jalapeño'
print s.encode('ascii', errors='xmlcharrefreplace')
