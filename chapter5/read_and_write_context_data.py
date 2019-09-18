#!coding=utf-8

"""
    读写文本数据
"""


# 需要读写各种不同编码的文本数据，如ASCII，UTF-8或UTF-16编码等
# 使用带有rt模式的open()函数读取文本文件，wt模式写文本文件，这仅适用于python3
# with open('xx', 'rt') as f:
#     for line in f:
#         print line


# 文件的读写操作默认使用系统编码，可以通过调用 sys.getdefaultencoding() 来得到。
# python2默认是ascii，python3默认是utf-8

# 另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和
# \r\n )。 默认情况下，Python会以统一模式处理换行符。 这种模式下，在读取文本的
# 时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。 类似的，在输出
# 时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，可以
# 给 open() 函数传入参数 newline=''，这个仅支持python3


# 如果出现这个错误，通常表示你读取文本时指定的编码不正确。 你最好仔细阅读说明并确认
# 你的文件编码是正确的(比如使用UTF-8而不是Latin-1编码或其他)。 如果编码错误还是存在
# 的话，你可以给 open() 函数传递一个可选的 errors 参数来处理这些错误。 下面是一些
# 处理常见错误的方法：仅支持python3
# >>> # Replace bad chars with Unicode U+fffd replacement char
# >>> f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
# >>> f.read()
# 'Spicy Jalape?o!'
# >>> # Ignore bad chars entirely
# >>> g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
# >>> g.read()
# 'Spicy Jalapeo!'
# >>>