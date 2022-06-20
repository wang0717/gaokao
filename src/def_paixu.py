#!/usr/bin/python
# -*- coding: UTF-8 -*-
#将两个列表进行相邻值排序
import def_quchazhi
chazhi=def_quchazhi.chazhi
    #定义求差值函数
def paixu(list1,list2,list3):
    a=list1
    b=list2
    c=list3
    t1=len(list1)
    t2=len(list2)
    t3=len(list3)
    long=min(t1, t2,t3)
    t=0
    while t<long:
        cha=chazhi(a,b,t)
        #定义cha为列表a与b第t项的差值列表
        Min=min(cha)
        if(Min)==cha[1]:
            a[t]=a[t]
            #列表1 第t项 与 列表2的第t项 值相同 列表1处不动；列表2不动
        elif(Min)==cha[0]:
            b.insert(t,b[t-1])
            c.insert(t,c[t-1])
            #列表1 第t项 与 列表2的第t-1项 值相同 列表1不动；列表2的第t项增加一项，值为t-1项的值
        elif(Min)==cha[2]:
            a.insert(t,"k")
            #列表1 第t项 与 列表2的第t+1项 值相同 列表1的第t项增加一项，值为空值；列表2不动
        t=t+1
    return(a,b,c)
if __name__ == "__main__":
    print(paixu([18, 23,27,34,36,43,51,54,61, 74, 78, 89, 103],[18, 21, 23, 27, 34, 36, 43, 51, 54, 61, 74, 78, 89, 103],[703, 702, 701, 700, 699, 698, 697, 696, 695, 694, 693, 692]))

