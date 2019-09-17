#!coding=utf-8

"""
    创建数据处理管道
"""


# 想以数据管道（类似UNIX管道）的方式迭代处理数据。比如，有一个大量的数据需要处理，
# 但不能将它们一次性放入内存。
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    find all filenames in directory tree thar match a shell wildcard pattern
    '''
    # path是当前目录，dirlist是当前目录下所有子目录，filelist是当前目录下所有文件
    # os.walk(dir)会首先遍历dir目录，然后递归遍历子目录，前提是有权限，
    # 算法是深度优先遍历
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:  # 这个文件名是包含绝对路径
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'r')
        # elif filename.endswith('.bz2'):  # 在python3可以指定模式为't'，表示以文本形式打开
        #     f = bz2.open(filename, 'rt')  # python2的bz2模块没有open()函数
        else:
            f = open(filename, 'r')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        for i in it:
            yield i


def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 现在你可以很容易的将这些函数连起来创建一个处理管道。 比如，为了查找包含
# 单词python的所有日志行，你可以这样做：
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)


# 以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询等。
#
# 为了理解上述代码，重点是要明白 yield 语句作为数据的生产者而 for 循环语句作为数据
# 的消费者。 当这些生成器被连在一起后，每个 yield 会将一个单独的数据元素传递给迭代
# 处理管道的下一阶段。 在例子最后部分， sum() 函数是最终的程序驱动者，每次从生成器
# 管道中提取出一个元素。

# David Beazley 在他的 Generator Tricks for Systems Programmers 教程中对于这种
# http://www.dabeaz.com/generators/
# 技术有非常深入的讲解。可以参考这个教程获取更多的信息。