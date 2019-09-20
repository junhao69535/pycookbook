#!coding=utf-8

"""
    只接受关键字参数的函数
"""


# 希望函数的某些参数强制使用关键字参数传递
# 以下语法仅支持python3
# def recv(maxsize, *, block):
#     pass

# recv(1024, True)  # TypeError
# recv(1024, block=True)