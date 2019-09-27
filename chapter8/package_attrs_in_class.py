#coding=utf-8

"""
    在类中封装属性名
"""


# Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果
# 1、单下划线前缀为保护类型
# 2、双下划线前缀为私有类型，在子类这个类型的变量会改名，在前面加上父类的名字
# 3、单下划线后缀用于与保留关键字区分：如lambda和lambda_
class Animal(object):
    _attr1 = 'test1'  # 这个变量子类能访问
    __attr2 = 'test2'   # 这个变量子类中会重命名为_Animal__attr2


class Dog(Animal):
    def getname(self):
        print self._attr1
        print dir(self)


Dog().getname()



