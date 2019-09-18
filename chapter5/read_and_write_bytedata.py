#!coding=utf-8

"""
    读写字节数据
"""


# 想读写二进制文件，比如图片，声音文件等等等。
# 使用模式为rb或wb的open()函数来处理
# with open('somefile.bin', 'wb') as f:
#     f.write('测试!')  #
#
#
# with open('somefile.bin', 'rb') as f:
#     print f.read()


# 在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串。
# 类似的，在写入的时候，必须保证参数是以字节形式对外暴露数据的对象(比如字节字符串，
# 字节数组对象等)。


# 二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入，而不需要中间转换
# 为自己对象。比如：
# import array
# nums = array.array('i', [1, 2, 3, 4])
# with open('somefile.bin', 'wb') as f:
#     f.write(nums)
# with open('somefile.bin', 'rb') as f:
#     nums = array.array('i', f.read())
#     print nums


# 很多对象还允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的
# 内存中去。比如：
# import array
# a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
# with open('data.bin', 'rb') as f:
#     f.readinto(a)

# 但是使用这种技术的时候需要格外小心，因为它通常具有平台相关性，并且可能会
# 依赖字长和字节顺序(高位优先和低位优先)。