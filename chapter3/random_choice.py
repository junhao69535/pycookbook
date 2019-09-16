#!coding=utf-8

"""
    随机选择
"""

# 想从一个序列中随机抽取若干元素，或者想生成几个随机数
# 可以使用random模块
import random
values = [1, 2, 3, 4, 5, 6]
print random.choice(values)  # 从列表中随机获取一个元素

# 为了提取出N个不同元素的样本用来做进一步的操作：
print random.sample(values, 2)  # 获取2个
print random.sample(values, 3)  # 获取3个

# 如果仅仅想打乱序列中元素的顺序：
random.shuffle(values)
print values

# 生成随机整数
print random.randint(0, 10)  # 从0到10随机生成一个数

# 为了生成0到1范围内均匀分布的浮点数：
print random.random()

# 获取N位随机位（二进制）的整数：
print random.getrandbits(200)


# random模块使用Mersenne Twister算法计算生成随机数。这时一个确定性算法。但是可以
# 通过random.seed()函数修改初始化种子。
random.seed()  # 种子基于系统时间
random.seed(12345)  # 种子基于这个整数
random.seed(b'bytedata')  # 种子基于这个字节字符串

# 更多内容请参考文档。
# 注：random模块不应该用在和密码学相关的程序，需要类似的功能，可以使用ssl模块中响应的函数
# 比如ssl.RAND_bytes()可以生成一个安全的随机字节序列。