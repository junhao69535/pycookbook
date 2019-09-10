#!coding=utf-8

"""
    保留最后N个元素
"""

# 保留有限历史记录可以使用collection.deque
from collections import deque
# deque()不给maxlen参数，默认为无限大小队列，这是一个双端队列，两端插入删除都是O(1)，
# 而列表开头插入和删除都是O(n)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print pline,
            print line,
            print '_' * 20


