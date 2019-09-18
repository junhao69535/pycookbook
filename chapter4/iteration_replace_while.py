#!coding=utf-8

"""
    迭代器代替while无限循环
"""


# 一个常见的IO操作可以如下：
CHUNKSIZE = 8192
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# 可以使用iter()代替
def reader2(s):
    for data in iter(lambda: s.recv(CHUNKSIZE), b''):  # 然后一个迭代器，知道它们的内容是b''
        process(data)


# iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记(结尾)值
# 作为输入参数。 当以这种方式使用的时候，它会创建一个迭代器， 这个迭代器会不断调用
# callable 对象直到返回值和标记值相等为止。