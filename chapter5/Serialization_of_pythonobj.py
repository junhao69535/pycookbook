#!coding=utf-8

"""
    序列化python对象
"""


# 需要将一个Python对象序列化为一个字节流，以便将它保存在一个文件，存储到数据库或者
# 通过网络传输它。
# 对于序列化最普遍的做法是使用pickle模块。为了将一个对象保存在一个文件中：
# import pickle
# with open('somefile', 'wb') as f:
#     data = 'this is a test!'
#     pickle.dump(data, f)
#
# with open('somefile', 'rb') as f:
#     data = pickle.load(f)
#     print data
#
#
# # 为了将一个对象存储为一个字符串，可以使用pickle.dumps()
# data = 'this is another test!'
# s = pickle.dumps(data)
# data = pickle.loads(s)
# print data


# pickle 是一种Python特有的自描述的数据编码。 通过自描述，被序列化后的数据包含
# 每个对象开始和结束以及它的类型信息。
# 还能序列化函数，类，还有接口，但是结果数据仅仅将它们的名称编码成对应的代码对象

# 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象， 比如
# 打开的文件，网络连接，线程，进程，栈帧等等。 用户自定义类可以通过提供 __getstate__()
# 和 __setstate__() 方法来绕过这些限制。 如果定义了这两个方法，pickle.dump() 就会调用
# __getstate__() 获取序列化的对象。 类似的，__setstate__() 在反序列化时被调用。


# pickle 对于大型的数据结构比如使用 array 或 numpy 模块创建的二进制数组效率并不是一个
# 高效的编码方式。 如果你需要移动大量的数组数据，你最好是先在一个文件中将其保存为数组
# 数据块或使用更高级的标准编码方式如HDF5 (需要第三方库的支持)。