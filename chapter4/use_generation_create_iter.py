#!coding=utf-8

"""
    使用生成器创建新的迭代模式
"""

# 想实现一个自定义迭代模式，跟普通的内置函数如range()和reversed()不一样


# 如果想实现一种新的迭代模式，使用一个生成器函数来定义它
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print n

print list(frange(0, 1, 0.125))


# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数
# 不同的是，生成器只能用于迭代操作
def countdown(n):
    print 'Starting to count from {}'.format(n)
    while n > 0:
        yield n  # 每次调用next都会把这里的n返回，然后停在这里，等待下一次调用next
        n -= 1
    print 'Done'


c = countdown(3)
print c  # 由于countdown()函数出现了yield，所以调用这个函数会返回一个生成器对象
print next(c)  # 1
print next(c)  # 2
print next(c)  # 3
print next(c)  # 4

# 当调用第一次next时，首次进入函数，先打印出'Starting to ……'，然后进入循环，此时n为3，
# 来到yield n这一步，会返回n给调用next()函数处，同时countdown()函数就停在了yield表达式
# 这里，调用next()函数出得到返回值，打印出3。第二次调用next时，不会从函数首部进入，而是
# 直接进入yield表达式，这时先执行n -= 1，while n > 0:，又来到了yield，返回n，并且函数
# 停在这里。剩下的都这样，除了最后一次调用next。最后一次调用next，恢复yield，执行
# n -= 1，此时n=0，跳出循环了，打印最后一句话'Done'，然后主动抛出StopIteration异常。

# 这里解释一下为什么for x in iter:等等的语句为什么没有抛出异常，那是因为for语句自动
# 处理了捕捉异常的细节