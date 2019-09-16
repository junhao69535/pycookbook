#!coding=utf-8

"""
    手动遍历迭代器
"""


# 想遍历一个可迭代对象中所有的元素，但是却不想使用for循环
# 使用next()函数并在代码中捕获StopIteration异常
def manual_iter():
    with open('passwd.txt') as f:
        try:
            while True:
                line = next(f)
                print line,
        except StopIteration:
            pass


# 通常,StopIteration用来指示迭代的结尾。然而，如果手动使用上面的代码，也可以
# 通过返回一个指定值来标记结尾：
with open('passwd.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print line,