#!coding=utf-8

"""
    获取文件夹中的文件列表
"""


# 想获取文件系统中某个目录下的所有文件列表
# 使用os.listdir()，结果会返回目录中所有文件列表，包括所有文件，子目录，符号链接等。
import os
print os.listdir(os.getcwd())


# 如果需要过滤数据，可以结合os.path的一些函数
# 获取所有文件
names = (name for name in os.listdir(os.getcwd()) if
         os.path.isfile(name))
# 获取所有目录
dirnames = (name for name in os.listdir(os.getcwd()) if
            os.path.isdir(name))
# 也可以使用字符串的startswith和endswith
pyfiles = [name for name in os.listdir(os.getcwd()) if
           name.endswith('.py')]
# 对于文件名的匹配，也可以考虑使用glob或fnmatch模块
import glob
pyfiles = glob.glob('xxx/*.py')
from fnmatch import fnmatch
pyfiles = (name for name in os.listdir(os.getcwd()) if
           fnmatch(name, '*.py'))


# 获取目录中的列表是很容易的，但是其返回结果只是目录中实体名列表而已。
# 如果你还想获取其他的元信息，比如文件大小，修改时间等等， 你或许还需要
# 使用到 os.path 模块中的函数或着 os.stat() 函数来收集数据。比如：


# 最后还有一点要注意的就是，有时候在处理文件名编码问题时候可能会出现一些问题。
# 通常来讲，函数 os.listdir() 返回的实体列表会根据系统默认的文件名编码来解码。