#!/usr/bin/python
# -*- coding: UTF-8 -*-
#定义取差值函数    列表1（第t+1项目）与列表2相邻位置的差值
def chazhi(list1,list2,t):
    a=list1
    b=list2
    t=t
    #print(a)            #列表1
    #print(b)            #列表2
    #print(a[t])         #第t+1项目
    x=abs(a[t]-b[t-1])  #与上
    y=abs(a[t]-b[t])    #与平
    z=abs(a[t]-b[t+1])  #与下
    return [x,y,z]
if __name__ == "__main__":
    m=chazhi([23,22,21,20,19],[22,21,20,19,18],1)
    print(m)
