#!coding=utf-8

"""
    在子类中扩展property
"""


# 在子类中，想要扩展定义在父类中的property的功能
class Person(object):
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print 'Getting name'
        return super(SubPerson, self).name

    @name.setter
    def name(self, value):
        print 'Setting name'
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print 'Deleteing name'
        super(SubPerson, SubPerson).name.__delete__(self)


# 如果你仅仅只想扩展property的某一个方法，那么可以像下面这样写：
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print 'Getting name'
        return super(SubPerson, SubPerson).name


# 在子类中扩展一个property可能会引起很多不易察觉的问题， 因为一个property其实是
# getter、setter 和 deleter 方法的集合，而不是单个方法。 因此，当你扩展一个
# property的时候，你需要先确定你是否要重新定义所有的方法还是说只修改其中某一个。

# 在第一个例子中，所有的property方法都被重新定义。 在每一个方法中，使用了 super()
# 来调用父类的实现。 在 setter 函数中使用 super(SubPerson, SubPerson).name.__set__
# (self, value) 的语句是没有错的。 为了委托给之前定义的setter方法，需要将控制权传递
# 给之前定义的name属性的 __set__() 方法。 不过，获取这个方法的唯一途径是使用类变量
# 而不是实例变量来访问它。 这也是为什么我们要使用 super(SubPerson, SubPerson) 的原因。


# 值得注意的是上面演示的第一种技术还可以被用来扩展一个描述器
# A descriptor
class String(object):
    def __init__(self, name):
        self.name = name

    # 实现了__get__和__set__方法的就是一个描述符
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with a descriptor
class Person(object):
    name = String('name')

    def __init__(self, name):
        self.name = name  # 这里会调用描述符的__set__方法


# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print 'Getting name'
        return super(SubPerson, SubPerson).name

    @name.setter
    def name(self, value):
        print 'Setting name to'.format(value)
        super(SubPerson, SubPerson).name.__set__(self, name)

    @name.deleter
    def name(self):
        print 'Deleting name'
        super(SubPerson, SubPerson).name.__delete__(self)
