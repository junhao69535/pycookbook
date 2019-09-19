#!coding=utf-8

"""
    忽略文件名编码
"""


# 想使用原始文件名执行文件的I/O操作，也就是说文件名并没有经过系统默认编码去
# 解码或编码过
# 默认情况下，所有的文件名都会根据sys.getfilesystemencoding()返回的文本编码
# 来编码或解码
import sys
print sys.getfilesystemencoding()
