#!coding=utf-8

"""
    字符串对其
"""

# 对于基本的字符串对齐操作，可以使用字符串的ljust()，rjust()和center()方法：
text = 'Hello World'
print text.ljust(20)
print text.rjust(20)
print text.center(20)

# 所有这么方法都接受一个可循啊的填充字符
print text.rjust(20, '=')
print text.center(20, '*')


# 函数 format() 同样可以用来很容易的对齐字符串。 你要做的就是使用 <,> 或者 ^ 字符
# 后面紧跟一个指定的宽度
print format(text, '>20')
print format(text, '<20')
print format(text, '^20')

# 如果需要指定一个非空格的填充字符，将它写到对齐字符的前面即可
print format(text, '=>20s')
print format(text, '*^20s')

# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中。比如：
print '{:>10s} {:>10s}'.format('Hello', 'World')

# format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得
# 它非常的通用。 比如，你可以用它来格式化数字：
x = 1.2345
print format(x, '>10')
print format(x, '^10.2f')
