#!coding=utf-8

"""
    字节到大整数的打包与解包
"""

# 有一个字节字符串并想将它解压成一个整数，或者，将一个大整数转换成
# 一个字节字符串

# 假设程序需要处理一个拥有128位长的16个元素的字节字符串
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# 为了将bytes解析为整数，使用int.from_bytes()方法，并像下面这样指定字节顺序
# 这个方法仅支持python3
# print len(data)
# print int.from_bytes(data, 'little')  # 小端模式，低位放在低字节

# x = 94522842520747284487117727783387188
# print x.to_bytes(16, 'big')  # 大端模式，低位放高字节


# 作为替代方案，可以利用struct模块来解压，但是这个模块对于整数的大小是有限制的。
import struct
hi, lo = struct.unpack('>QQ', data)
print (hi << 64) + lo


# a = 'hello\x7F'
# b = u'hello\x80'.encode('utf-8')
# print type(b)
# print a == b
# print a.decode('ascii')
# print b.decode('utf-8')
# c = bytearray(u'\x64\x80\x64', encoding='utf-8')  # 这一步会出错，因为它会这样做'\x80'.decode('ascii').encode('utf-8')
# print c.decode('utf-8')
#
# s = u'测试'
# s1 = s.encode('gbk')
# print s1.decode('gbk')
a = '\xE5\x85\x84\xE5\xBC\x9F\xE9\x9A\xBE\xE5\xBD\x93 \xE6\x9D\x9C\xE6\xAD\x8C'
print a.decode('utf-8')