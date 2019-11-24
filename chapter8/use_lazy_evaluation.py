#!coding=utf-8

"""
    使用延迟计算属性
"""


# 你想将一个只读属性定义成一个property，并且只在访问的时候才会计算结果。
# 但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算。
# 定义一个延迟属性的一种高效方法是通过使用一个描述器类：
class lazyproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        # 这个类Circle会在类字典__dict__添加这个函数，而这个函数经过修饰器之后返回
        # 一个lazyproperty实例，即__dict__['area'] = lazyproperty(area)，因此
        # 这个函数等同于实现了描述器协议，可以作为属性被访问
        print 'Computing area'
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print 'Computing perimeter'
        return 2 * math.pi * self.radius


c = Circle(4.0)
print c.area
print c.perimeter
print c.area
print c.perimeter
# 发现'Computing area'和'Computing perimeter'只会打印一次，这是因为仅仅实现了
# __get__()方法，它会比通常的具有更弱的绑定。在这种情况下（只定义了__get__())，
# 只有当被访问属性不在实例底层的字典中时 __get__() 方法才会被触发。而我们在
# lazyproperty的__get__()中给实例字典添加了属性，因此后面会直接访问实例字典
# 中的变量。
# 基于上面实现了延迟计算，lazyproperty 类利用这一点，使用 __get__() 方法在实例中
# 存储计算出来的值， 这个实例使用相同的名字作为它的property。 这样一来，结果值被
# 存储在实例字典中并且以后就不需要再去计算这个property了。
c = Circle(4.0)
print vars(c)  # 延迟计算了，当没有使用c.area时，不存在这个属性
c.area
print vars(c)
del c.area
print vars(c)
# 这种方案有一个小缺陷就是计算出的值被创建后是可以被修改的。
# 为什么可以修改，因此area已经作为实例字典中的一个元素，修改它等同于修改实例字典
# 中的某个元素的值

