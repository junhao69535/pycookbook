#!coding=utf-8

"""
    创建不调用init方法的实例
"""


# 创建一个实例，绕过执行__init__()方法。
# 可以通过__new__()方法创建一个未初始化的实例，考虑如下的类：
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# 下面是不使用__init__()创建Date实例
d = Date.__new__(Date)
# d.year  # 会报错，因为不存在这个属性

# 结果可以看到，这个Date实例的属性year还不存在，所以你需要手动初始化：
data = {'year': 2012, 'month': 8, 'day': 29}
for key, value in data.items():
    setattr(d, key, value)


print d.year
print d.month


# 当我们在反序列对象或者实现某个类方法构造函数时需要绕过 __init__() 方法来创建对象。
import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


# 当你通过这种非常规方式来创建实例的时候，最好不要直接去访问底层实例字典，除非你真的清楚所有细节。 否则的话，
# 如果这个类使用了 __slots__ 、properties 、descriptors 或其他高级技术的时候代码就会失效。 而这时候使用
# setattr() 方法会让你的代码变得更加通用。