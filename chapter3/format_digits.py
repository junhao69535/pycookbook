#!coding=utf-8

"""
    数字的格式化输出
"""

# 需要将数字格式化输出，并控制数字的位数、对齐、千位分隔符和其他的细节
# 格式化输出单个数字的时候，可以使用内置的format()函数
x = 1234.56789
print format(x, '.2f')  # 保留两位小数
print format(x, '>10.1f')  # 右对齐，10个字符宽度，保留一位小鼠
print format(x, '<10.1f')  # 左对齐，10个字符宽度，保留一位小鼠
print format(x, '^10.1f')  # 居中对齐，10个字符宽度，保留一位小鼠
print format(x, ',')  # 增加千位分隔符
print format(x, ',.1f')  # 增加千位分隔符并保留一个小数


# 如果想使用指数记法，将f改成e或者E即可。其实f和e之类的与c语言格式说明一样
print format(x, 'e')
print format(x, '0.2E')

# 同时指定宽度和精度一般形式是'[<>^]?width[,]?(.digits)?'，其中width和digits为整数，
# ？代表可选部分，出现0次或者1次。
# 同样的操作能使用在字符串的format()方法中。
print 'The value is {:0,.2f}'.format(x)

