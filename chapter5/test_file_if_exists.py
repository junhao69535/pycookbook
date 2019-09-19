#!coding=utf-8


"""
    测试一个文件或目录是否存在
"""


# 使用os.path模块来测试一个文件或目录是否存在
import os
print os.path.exists(os.getcwd())
print os.path.exists('/opt')


# 想进一步测试文件是什么类型的
print os.path.isfile('/etv/passwd')
print os.path.isdir(os.getcwd())
# 判断是否是符号链接
print os.path.islink('/usr/local/bin/python3')
# 获取符号链接的真实路径
print os.path.realpath('/usr/local/bin/python3')


# 想获取文件的大小或者三个日期（change_time,modify_time,access_time)
# 获取文件大小
print os.path.getsize(os.path.join(os.getcwd(), 'test.txt'))
# 获取文件的获取时间，access_time,如果访问或修改了文件内容，这个时间会改变
print os.path.getatime(os.path.join(os.getcwd(), 'test.txt'))
# 获取文件的修改时间，modify_time，如果文件修改了会改变这个时间
print os.path.getmtime(os.path.join(os.getcwd(), 'test.txt'))
# 获取文件的改变时间，如果文件修改了，或者文件的属性修改了（chmod），这个时间会改变
print os.path.getctime(os.path.join(os.getcwd(), 'test.txt'))


# 最后，注意在获取文件信息时，需要考虑文件权限！使用os.stat()得到文件权限。