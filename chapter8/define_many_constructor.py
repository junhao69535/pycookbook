#!coding=utf-8

"""
    在类中定义多个构造器
"""


# 实现一个类，除了使用 __init__() 方法外，还有其他方式可以初始化它。
# 为了实现多个构造器，需要使用类方法
import time

class Date(object):
    """方法一：使用类方法"""
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# 直接调用类方法
a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate


# 类方法的一个主要用途就是定义多个构造器，继承也会继承类方法
class NewDate(Date):
    pass


c = NewDate(2012, 12, 21)
d = NewDate.today()