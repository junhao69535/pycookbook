#!coding=utf-8

"""
    合并拼接字符串
"""

# 如果想要合并的字符串是在一个序列或者iterable中，最快的方式的使用join()方法
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print ' '.join(parts)
print ','.join(parts)
print ''.join(parts)

# 如果你仅仅只是合并少数几个字符串，使用加号(+)通常已经足够了
a = 'Is Chicago'
b = 'Not Chicago?'
print a + ' ' + b

# 如果你想在源码中将两个字面字符串合并起来，你只需要简单的将它们放到一起，不需要用加号(+)
print 'Hello' 'World'

# 加号操作性能很低，应该避免以下做法
s = ''
for p in parts:
    s += p

# 改用join()
data = ['ACME', 50, 91, 1]
print ','.join(str(d) for d in data)


# 当混合使用I/O操作和字符串连接操作的时候，有时候需要仔细研究你的程序。 比如，考虑
# 下面的两端代码片段：
# Version 1 (string concatenation)
# f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# 如果两个字符串很小，那么第一个版本性能会更好些，因为I/O系统调用天生就慢。 另外
# 一方面，如果两个字符串很大，那么第二个版本可能会更加高效， 因为它避免了创建一个
# 很大的临时结果并且要复制大量的内存块数据。 还是那句话，有时候是需要根据你的应用
# 程序特点来决定应该使用哪种方案。
