#!coding=utf-8

"""
    结合时区的日期操作
"""

# 你有一个安排在2012年12月21日早上9:30的电话会议，地点在芝加哥。 而你的朋友在
# 印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？

# 对于所有涉及时区的问题，都应该使用pytz模块
from datetime import datetime, timedelta
from pytz import timezone
import pytz
d = datetime(2012, 12, 21, 9, 30, 0)
central = timezone('US/Central')  # 先创建一个本地时间的对象
loc_d = central.localize(d)  # 本地化日期
print loc_d

# 转换成班加罗尔时间
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print bang_d


# 为了处理更清晰，处理本地化日期通常的策略先将所有日期转换位UTC时间，并用它来执行所有
# 的中间存储和操作：
utc_d = loc_d.astimezone(pytz.utc)
# 一旦转换为UTC，你就不用去担心跟夏令时相关的问题了。 因此，你可以跟之前一样放心的执
# 行常见的日期计算。 当你想将输出变为本地时间的时候，使用合适的时区去转换下就行了
later_utc = utc_d + timedelta(minutes=30)
print later_utc.astimezone(central)

# 当涉及到时区操作的时候，有个问题就是我们如何得到时区的名称。 比如，在这个例子中，
# 我们如何知道“Asia/Kolkata”就是印度对应的时区名呢？ 为了查找，可以使用ISO 3166国家
# 代码作为关键字去查阅字典 pytz.country_timezones

# import time
# print time.accept2dyear
# print time.altzone
# print time.clock()
# print time.time()  # 得到一个当前时间的10位时间戳
# print time.ctime(time.time())  # 将时间戳转换成日期字符串，接受10位时间戳
# print time.gmtime(time.time())  # 将时间戳转换成时间信息结构体，接受10位时间戳
# print time.localtime(time.time())  # 作用同gmtime()
# print time.mktime(time.localtime(time.time()))  # 把一个时间信息结构体转换成unix时间戳
# print time.asctime(time.localtime(time.time()))  # 将一个时间信息结构体转换成日期字符串，和ctime()一样，只是接受的参数不一样
# print time.sleep(2)  # 休眠2秒
# print time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 将一个时间信息结构体转换成对应格式的日期字符串
# print time.strptime('2019-9-16', '%Y-%m-%d')  # 将str字符串匹配格式字符串转换成一个时间信息结构体
# print time.struct_time(time.localtime(time.time()))
# print time.time()  # 获取unix时间戳10位
# print time.timezone
# print time.tzname