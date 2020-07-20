# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : flatten.py
# Time       ：2020/6/13 13:28
# Author     ：eastonliu
# version    ：python 3.8
# Description：用递归将序列展开
"""
from collections.abc import *


def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)
        else:
            output_arr.append(ele)
    return output_arr


if __name__ == '__main__':
    l = flatten([[1, 5, (8, 6)], [7, 3]])
    print(l)
