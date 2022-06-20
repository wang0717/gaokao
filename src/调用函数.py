#!/usr/bin/python
# -*- coding: UTF-8 -*-
#调用其它文件里的函数
import def_min

a=1
b=a
b=b+1
print(b)
if __name__ == "__main__":              #只能在此函数里使用
    a=def_min.min
print(a([6,8,4]))