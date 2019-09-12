#!coding=utf-8

"""
    多行匹配模式
"""

# 当使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配
# 这个问题很典型出现再当用点'.'去匹配任意字符时，忘记'.'不能匹配换行符。
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print comment.findall(text1)
print comment.findall(text2)

# 解决办法：修改模式字符串，增加对换行的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment.findall(text2)
# 在这个模式中， (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来
# 做匹配，而不能通过单独捕获或者编号的组)。


# re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它
# 可以让正则表达式中的点(.)匹配包括换行符在内的任意字符。
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment.findall(text2)

# 对于简单的情况使用 re.DOTALL 标记参数工作的很好， 但是如果模式非常复杂
# 或者是为了构造字符串令牌而将多个模式合并起来(2.18节有详细描述)， 这时候
# 使用这个标记参数就可能出现一些问题。 如果让你选择的话，最好还是定义自己
# 的正则表达式模式，这样它可以在不需要额外的标记参数下也能工作的很好。