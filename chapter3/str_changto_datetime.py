#!coding=utf-8

"""
    字符串转换位日期
"""

# 想把字符串的日期转换成datetime对象
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()  # 等价于today()方法
diff = z - y
print diff

# 想将datetime转换成格式化字符串
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print nice_z


# strptime()的性能很差，如果想获取更好的性能，需要自己实现：
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
