#!coding=utf-8

"""
    二八十六进制整数
"""

# 需要转换或者输出使用二进制，八进制或者十六进制表示的整数
# 分别使用bin(),oct()或hex()函数
x = 1234
print bin(x)
print oct(x)
print hex(x)

# 如果不像输入ob,ox之类的前缀，可以使用format()函数
print format(x, 'b')
print format(x, 'o')
print format(x, 'x')

# 整数是有符号的，处理负数时，输出也会包含一个负号
x = -1234
print format(x, 'b')

# 如果想产生一个无符号值，需要增加一个指示最大位长度的值。比如为了显示32位的值
print format(2**32 + x, 'b')  # 等同于求补码，加上2**32是为了补位，使其能显示32位
print format(x & 0xffffffff, 'b')  # 同上


# 为了以不同的进制转换整数字符串，简单的使用带有进制的 int() 函数即可：
print int('4d2', 16)
print int('10011010010', 2)

# 最后，使用八进制的程序员有一点需要注意下。 Python指定八进制数的语法跟其他语言
# 稍有不同。比如，如果你像下面这样指定八进制，会出现语法错误：
# import os
# os.chmod('script.py', 0755)  # 会报错

# 需要确保八进制数前缀时'0o'
# os.chmod('script.py', 0o755)