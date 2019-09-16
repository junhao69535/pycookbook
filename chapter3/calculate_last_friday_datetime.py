#!coding=utf-8

"""
    计算最后一个周五的日期
"""

# 需要查找星期中某一天最后出现的日期，比如星期五
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    print 'start_date:{}'.format(start_date)
    day_num = start_date.weekday()  # 返回这个日期是周几，0是周一……
    print 'day_num:{}'.format(day_num)
    day_num_target = weekdays.index(dayname)
    print 'day_num_target:{}'.format(day_num_target)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print get_previous_byday('Monday')

# 上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)，
# 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期减去那个时间
# 差即得到结果日期。

# 如果你要像这样执行大量的日期计算的话，你最好安装第三方包 python-dateutil 来代替。