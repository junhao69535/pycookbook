#!coding=utf-8

"""
    实现一个优先级队列
"""

# 实现一个按优先级排序的队列，每次pop都是返回优先级最高的元素
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 实现的关键在于(-priority, self._index, item),这个元组是可以比较的，
        # 先按照-priority比较，如果相同，再按照self._index比较。
        # 就是因为可比较实现优先级，因为heappush维护了一个最小堆
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 因为给push是一个元组，取出item


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print q.pop()
print q.pop()
print q.pop()
print q.pop()