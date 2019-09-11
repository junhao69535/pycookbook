#!coding=utf-8

"""
    从字典中提取子集
"""

# 最简单方式是字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print p1
print p2