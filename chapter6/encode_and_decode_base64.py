#!coding=utf-8

"""
    编码解码BAse64数据
"""


# 需要使用Base64格式解码或编码二进制数据
s = 'hello'
import base64
# 编码
a = base64.b64encode(s)
print a
# 解码
print base64.b64decode(a)

# Base64编码仅仅用于面向字节的数据比如字节字符串和字节数组。 此外，
# 编码处理的输出结果总是一个字节字符串。 如果你想混合使用Base64编码
# 的数据和Unicode文本，你必须添加一个额外的解码步骤。

# 当解码Base64的时候，字节字符串和Unicode文本都可以作为参数。 但是，
# Unicode字符串只能包含ASCII字符。