#!coding=utf-8

"""
    读写CSV数据
"""

# 可以使用csv库
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)  # 返回的是生成器
    headers = next(f_csv)
    for row in f_csv:
        print row


# 可以使用命名元组访问：
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headerings = next(f_csv)
    Row = namedtuple('Row', headerings)
    for r in f_csv:
        row = Row(*r)
        print row.Symbol, row.Price


# 写入
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
with open('stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)


# 最后，如果你读取CSV数据的目的是做数据分析和统计的话， 你可能需要看一看 Pandas 包。