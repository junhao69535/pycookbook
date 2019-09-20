#!coding=utf-8

"""
    解析简单的XML数据
"""


# 可以使用xml.etree.ElementTree模块
from urllib2 import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print title
    print date
    print link