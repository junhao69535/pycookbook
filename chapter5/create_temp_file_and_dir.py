#!coding=utf-8

"""
    需要创建一个临时的文件或目录，使用完自动销毁
"""


from tempfile import TemporaryFile

with TemporaryFile('w') as f:
    f.write('Hello World!\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()
    print data