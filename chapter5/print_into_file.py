#!coding=utf-8

"""
    打印输出至文件中
"""


# 想将print()函数的输出重定向到一个文件中
# 注python2往文件写内容都是先把内容转换为字节字符串，因此如果要写unicode的字符串必须
# 先编码，如u'测试！'.encode('utf-8')。
with open('test.txt', 'w') as f:
    print >> f, 'Hello World!'
    # 这种重定向只能覆盖，不能追加
    # python3写法print('Hello World!', file=f)
