#!coding=utf-8

"""
    审查清理文本字符串
"""

# 一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉
# 比如，你可能想消除整个区间上的字符或者去除变音符。 为了这样做，你可以使用经常会被
# 忽视的 str.translate() 方法。
# 这个方法python2和python3有区别
s = 'pýtĥöñ\fis\tawesome\r\n'
print s
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
# a = s.translate('')
# print a
