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

# 一般来讲，JSON解码会根据提供的数据创建dicts或lists。 如果你想要创建其他类型的对象，
# 可以给 json.loads() 传递object_pairs_hook或object_hook参数。
from collections import OrderedDict
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print data


# 下面是如何将一个JSON字典转换成一个Python对象：
class JSONObjec(object):
    def __init__(self, d):
        self.__dict__ = d
data = json.loads(s, object_hook=JSONObjec)
print data.name
# 最后一个例子中，JSON解码后的字典作为一个单个参数传递给 __init__() 。

# 在编码JSON的时候，还有一些选项很有用。 如果你想获得漂亮的格式化字符串后输出，
# 可以使用 json.dumps() 的indent参数。 它会使得输出和pprint()函数效果类似。

# 对象实例通常是不可JSON序列化的，如果你想序列化对象实例，你可以提供一个函数，
# 它的输入是一个实例，返回一个可序列化的字典。
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# 如果你想反过来获取这个实例，可以这样做：
classes = {
    'Point' : Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d