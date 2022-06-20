#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义最小值函数 一个列表的最小值
def min(my_list):
    min = my_list[0]
    t = len(my_list)
    for i in range(t):
        if my_list[i] < min:
            min = my_list[i]
    return min


if __name__ == "__main__":
    m = min([2, 3, 1])
    print(m)
