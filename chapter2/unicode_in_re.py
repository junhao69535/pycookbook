#!coding=utf-8

"""
    在正则式中使用Unicode
"""

# 默认情况下 re 模块已经对一些Unicode字符类有了基本的支持。 比如，
# \\d 已经匹配任意的unicode数字字符了：
import re
num = re.compile(u'\d+')
print num.match('123')
print num.match(u'\u0661\u0662\u0663')

pat = re.compile(u'stra\u00dfe', re.IGNORECASE)
s = u'straße'
print pat.match(s)  # Matches

# 混合使用Unicode和正则表达式通常会让你抓狂。 如果你真的打算这样做的话，
# 最好考虑下安装第三方正则式库， 它们会为Unicode的大小写转换和其他大量
# 有趣特性提供全面的支持，包括模糊匹配。
