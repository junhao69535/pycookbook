#!coding=utf-8

"""
    计算当前月份的日期范围
"""

# 需要循环当前月份的每一天，想找到一个计算这个日期范围的高效方法
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = datetime.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print _
    print days_in_month
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


print get_month_range()