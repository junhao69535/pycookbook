#!coding=utf-8

"""
    将字节写入文本文件
"""


# 想在文本模式打开的文件中写入原始的字节数据
import sys
text = sys.stdin.read()
sys.stdout.write(text)
sys.stdout.flush()
