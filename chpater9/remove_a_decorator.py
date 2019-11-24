#!coding=utf-8

"""
    解除一个装饰器
"""

# 一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。
# 假设装饰器是通过 @wraps (参考9.2小节)来实现的，那么你可以通过访问 __wrapped__ 属性来访问原始函数：
# 但这种特性只支持python3
# @somedecorator
# def add(x, y):
#     return x + y
# orig_add = add.__wrapped__
# orig_add(3, 4)

# 如果有多个包装器，那么访问 __wrapped__ 属性的行为是不可预知的，应该避免这样做。

# 结论，直接调原函数不就好了吗？