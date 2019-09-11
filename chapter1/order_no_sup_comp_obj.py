#!coding=utf-8

"""
    排序不支持原生比较的独享
"""

# 内置的sorted()函数有一个关键字参数key,可以传入一个callable，这是排序的标准
# 比如app里有一个User实例，并且希望通过他们的user_id进行排序，可以提供一个以
# User实例作为输入并输出对应user_id值的callable对象
class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = (User(23), User(3), User(99))
    print users
    print sorted(users, key=lambda u: u.user_id)


# 也可以使用operator.attrgettr()
from operator import attrgetter
users = (User(23), User(3), User(99))
print sorted(users, key=attrgetter('user_id'))

# operator.attrgettr()性能更好