#!coding=utf-8

"""
    字典的运算
"""

# 在字典中执行一些计算操作（比如求最小值，最大值，排序）

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 对字典值执行计算操作，通常需要使用zip()函数先将键和值翻转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print min_price, max_price

# 类似的，可以使用zip()和sorted()函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print prices_sorted
# 注意：zip()创建的是一个只能访问一次的迭代器（生成器）

# 当多个实体拥有相同的值时，键会决定返回结果。