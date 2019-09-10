#!coding=utf-8

"""
    解压序列赋值给多个变量
"""

# 任何可迭代对象都可以解包,左边变量必须很解包得到的变量数量一致
p = (4, 5)
x, y = p
print x, y

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print name, shares, price, date

name, shares, price, (year, mon, day) = data
print name, shares, price, year, mon, day

# 若想丢弃某些值，可以使用占位符'_'
_, shares, price, _ = data
print shares, price