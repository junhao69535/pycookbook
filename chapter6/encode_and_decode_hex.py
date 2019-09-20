#!coding=utf-8

"""
    解码和编码十六进制数
"""


# 想将一个十六进制字符串解码成一个字节字符串或者将一个字节字符串编码成一个十六进制
# 字符串。
# 如果只是简单的解码或编码一个十六进制的原始字符串，可以使用binascii模块
s = 'hello'
import binascii
# 编码
h = binascii.b2a_hex(s)
print h
# 解码
print binascii.a2b_hex(h)


# 类似的功能同样可以在base64模块中找到
import base64
h = base64.b16encode(s)
print h
print base64.b16decode(h)


# 大部分情况下，通过使用上述的函数来转换十六进制是很简单的。 上面两种技术的主要
# 不同在于大小写的处理。 函数 base64.b16decode() 和 base64.b16encode() 只能
# 操作大写形式的十六进制字母， 而 binascii 模块中的函数大小写都能处理。

# 在解码十六进制数时，函数 b16decode() 和 a2b_hex() 可以接受字节或unicode字符串。
# 但是，unicode字符串必须仅仅只包含ASCII编码的十六进制数。