# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : fib.py
# Time       ：2020/6/13 22:21
# Author     ：eastonliu
# version    ：python 3.8
# Description：斐波那契数列
"""


def fib(n):
    if n <= 0:
        return '请输入大于0的正整数'
    if not isinstance(n, int):
        return '请输入整数'
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    pre1 = 0
    pre2 = 1
    seq = [0, 1]
    for i in range(3, n + 1):
        count = pre1 + pre2
        seq.append(count)
        pre1 = pre2
        pre2 = count
        i += 1
    return seq


if __name__ == '__main__':
    fib_seq = fib(-6)
    print(fib_seq)
