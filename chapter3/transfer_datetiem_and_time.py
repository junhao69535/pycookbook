#!coding=utf-8

"""
    基本的日期与时间转换
"""

# 为了执行不同时间单位的转换和计算，使用datetime模块。比如，为了表示一个时间段，
# 可以创建一个timedelta实例：
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print c.days
print c.seconds
print c.seconds / 3600  # c.seconds获取的仅仅是针对hours得到的，
print c.total_seconds() / 3600  # 求总共的小时


# 如果想表示指定的日期和时间，先创建一个datetime实例然后使用标准的数学运算来操作它们：
from datetime import datetime
a = datetime(2012, 9, 23)
print a + timedelta(days=10)
b = datetime(2012, 12, 11)
d = b - a
print d.days
now = datetime.today()
print now
print now + timedelta(minutes=10)

# 在计算的时候，要注意datetime会自动处理闰年

# 对大多数基本的日期和时间y处理问题， datetime 模块已经足够了。 如果你需要执行更加复杂
# 的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块
