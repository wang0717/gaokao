#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd ##读取excel文件
import xlwt ##写入excel文件
from xlutils.copy import copy #写入excel文件
   #打开需要修改的excel文件
old_excel = xlrd.open_workbook(r'/Users/admins/Desktop/a.xlsx', formatting_info=True)
    
# 将操作文件对象拷贝，变成可写的workbook对象  
new_excel = copy(old_excel)
def write(my_num,my_list1,my_list2,my_list3):
    ws = new_excel.get_sheet(my_num)
    long=min(len(my_list1),len(my_list2))
    t=0  
    while t<long :
        ws.write(t+1, 0, my_list1[t])
        ws.write(t+1, 1, my_list2[t])
        ws.write(t+1, 2, my_list3[t])
        t=t+1
        
def write_excel(list1,list2,list3,list4,list5,txt):
    print("写入Excel表开始")
    shuju1=list1
    shuju2=list2
    shuju3=list3
    shuju4=list4
    shuju5=list5
    q=txt
    write(0,shuju1[0],shuju1[1],shuju1[2])
    write(1,shuju2[0],shuju2[1],shuju2[2])
    write(2,shuju3[0],shuju3[1],shuju3[2])
    write(3,shuju4[0],shuju4[1],shuju4[2])
    write(4,shuju5[0],shuju5[1],shuju5[2])
    #写入excel的第行，第列，某数据
    #ws.write(2,3,4)
    
    #重新保存为新excel
    new_excel.save('/Users/admins/Desktop/\%s.xlsx'%q)

    print("写入Excel表成功")