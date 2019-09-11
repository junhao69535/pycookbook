#!coding=utf-8

"""
    序列中出现次数最多的元素
"""

# collections.Counter类就是为这类问题设计的
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print top_three


# Counter对象接受任意可哈希元素构成的序列对象。底层实现上Counter对象就是一个字典，
# 将元素映射到它出现的次数上
print word_counts['not']
print word_counts['eyes']


# 如果想手动增加计数，可以使用加法
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print word_counts['eyes']

# 也可以使用update()
# word_counts.update(morewords)


# Counter实例也可以跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b
print a
print b
print c
print d