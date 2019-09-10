#!coding=utf-8

"""
    查找最大或最小的N个元素
"""

# 从一个集合中获得最大或者最小的N个元素列表
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print heapq.nlargest(3, nums)  # 维护一个最小堆
print heapq.nsmallest(3, nums)  # 维护一个最大堆

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda  s: s['price'])
print cheap
print expensive

# 如果想在一个集合中最小或最大的N个元素，并且N小于集合元素数量，那么heapqq能提供很好
# 的性能，底层实现是堆，时间复杂度为O(logn)
heap = list(nums)
heapq.heapify(heap)  # 把列表转换成堆，为最小堆
print heap
# 获取最小的三个数, heappop每弹出一个元素会重新维护堆
print heapq.heappop(heap), heapq.heappop(heap), heapq.heappop(heap)

# 当要查找的元素个数N相对比较少时，nlargest()和nsmallest()比较合适。如果要唯一一个最大或
# 最小的元素，使用max()和min()更快。如果N接近集合大小，应该先排序再切片比较好。
# sorted(items)[:N]或者sorted(items)[-N:]