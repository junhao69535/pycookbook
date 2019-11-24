#!coding=utf-8
"""
    以编程方式定义类
"""
# 你在写一段代码，最终需要创建一个新的类对象。你考虑将类的定义源代码以字符串的形式发布出去，
# 并且使用函数比如 exec() 来执行它，但是你想寻找一个更加优雅的解决方案。
# 你可以使用函数 types.new_class() 来初始化新的类对象。 你需要做的只是提供类的名字、
# 父类元组、关键字参数，以及一个用成员变量填充类字典的回调函数。例如：
# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    "__init__": __init__,
    "cost": cost,
}


# Make a class
import types


Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))
# 仅支持python3