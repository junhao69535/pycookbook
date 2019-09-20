#!coding=utf-8

"""
    读写二进制数组数据
"""


# 想读写一个二进制数组的结构化数据到Python元组中。
from struct import Struct
def write_records(records, format, f):
    '''
    write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


records = [(1, 2.3, 4.5),
           (6, 7.8, 9.0),
           (12, 13.4, 56.7)
           ]
with open('data.b', 'wb') as f:
    write_records(records, '<idd', f)