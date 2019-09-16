#!coding=utf-8

"""
    字符串令牌解析
"""

# 假如有一个字符串，想从左到右将其解析为一个令牌流
text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import re
NMAE = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

# 只有python3有能用
# master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner = master_pat.scanner('foo = 42')