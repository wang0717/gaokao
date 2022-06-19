#!/usr/bin/python
# -*- coding: UTF-8 -*-

import def_read_excel

read_excel=def_read_excel.read_excel

def shuju(num):
    n=num-1
    list1=read_excel(n)[0]
    list2=read_excel(n)[1]
    list3=read_excel(n)[2]
    year=[list1,list2,list3]
    return(year)
#整理某年的数据：第一列，第二列，第三列
print("按年份整理成功")
print("一表单数据：")
print("往年：",shuju(1)[0])
print("本年：",shuju(1)[1])
print("本年：",shuju(1)[2])