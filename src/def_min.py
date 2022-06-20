#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义最小值函数 一个列表的最小值
def min (list):
    min=list[0]
    t=len(list)
    for i in range(t):
        if list[i]<min:
            min=list[i]
    return min
if __name__ == "__main__":
    m=min([2,3,1])
    print(m)
