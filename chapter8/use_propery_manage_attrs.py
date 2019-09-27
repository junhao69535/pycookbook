#!coding=utf-8

"""
    创建可管理的属性
"""


# 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。
class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name  # 这里会调用@first_name.setter修饰的first_name()方法

    # Getter function
    @property
    def first_name(self):  # 当外部访问属性first_name就会调用这个函数
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):  # 当外部修改属性first_name就会调用这个函数
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value  # 设置了一个保护变量

    # Deleter function(optional)
    @first_name.deleter
    def first_name(self):  # 调用del删除这个属性时会调用这个函数
        raise AttributeError("Can't delete attribute")


# 上述代码中有三个相关联的方法，这三个方法的名字都必须一样。 第一个方法是一个 getter 函数
# ，它使得 first_name 成为一个属性。 其他两个方法给 first_name 属性添加了 setter 和
# deleter 函数。 需要强调的是只有在 first_name 属性被创建后，后面的两个装饰器只有
# @first_name.setter 和 @first_name.deleter 才能被定义。即没有@propery修饰的方法，
# 后面两个装饰器会报错。


p = Person('Jack')
print p.first_name  # 调用@property修饰的first_name()方法
p.first_name = 5  # 调用@first_name.setter修饰的first_name()方法
del p.first_name  # 调用@first_name.deleter修饰的first_name()方法


# 不要写有大量重复代码的property定义，重复代码会导致臃肿、易出错和丑陋的程序。好消息是，
# 通过使用装饰器或闭包，有很多种更好的方法来完成同样的事情。 可以参考8.9和9.21小节的内容。