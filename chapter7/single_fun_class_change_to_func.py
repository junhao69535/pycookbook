#!coding=utf-8

"""
    将单个方法的类转换为函数
"""


# 有一个除了__init__()方法外只定义了一个方法的类。为了简化，想转换成一个函数
# 大多情况下可以使用闭包：
from urllib2 import urlopen


class UrlTemplate(object):
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format(**kwargs))


yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
    print line.decode('utf-8')


# 可以使用闭包函数
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format(**kwargs))
    return opener


yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sllclv'):
    print line.decode('utf-8')


# 任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使用闭包。