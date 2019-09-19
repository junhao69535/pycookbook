#!coding=utf-8

"""
    读写JSON数据
"""


# json模块提供了json数据的编码和解码
import json
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)
print json_str
data = json.loads(json_str)
print data

# 如果处理文件，用json.dump()和json.load()

# JSON编码支持的基本数据类型为 None ， bool ， int ， float 和 str ，
# 以及包含这些类型数据的lists，tuples和dictionaries。


# 如果你试着去检查JSON解码后的数据，你通常很难通过简单的打印来确定它的结构，
# 特别是当数据的嵌套结构层次很深或者包含大量的字段时。 为了解决这个问题，可以
# 考虑使用pprint模块的 pprint() 函数来代替普通的 print() 函数。