#!coding=utf-8

"""
    实现迭代器协议
"""


# 想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单办法。
# 在一个对象上实现迭代最简单的方式是使用生成器函数。现在实现一个深度优先遍历：
class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self  # 第一次返回根节点
        for c in self:
            for i in c.depth_first():  # 替代yield from c.depth_first()
                yield i  # python2没有yield from，只能这样实现


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():
    print ch


# Python的迭代协议要求一个 __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器
# 对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。 但是，实现
# 这些通常会比较繁琐。 下面我们演示下这种方式，如何使用一个关联迭代器类重新实现
# depth_first() 方法：
class Node2(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """
        Depth-first traversal
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._child_iter is None:
            self._child_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._child_iter).depth_first()
            return next(self)