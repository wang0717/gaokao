#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd #读取excel文件
import xlwt #写入excel文件
from xlutils.copy import copy #写入excel文件
import def_qukong #调用去空格函数
qukong=def_qukong.qukong
print("读取Excel表开始")
def read_excel(sheet_num,list_num):      #读取excel表第sheet_num个sheet页面的前三列数据
    num1 = sheet_num-1                # 定义选取那个sheet界面
    num2 = list_num-1                 # 定义选取sheet界面哪列数据
    workbook = xlrd.open_workbook(r'/Users/admins/Desktop/a.xlsx') #读取所在位置的excel文件
    sheet_names = workbook.sheet_names()                            #读取excel的所有sheet名称
    sheet_num = workbook.sheet_by_name(sheet_names[num1])            #读取excel表中第sheet_num个sheet页面数据
    cols = sheet_num.col_values(num2)                                 #读取sheet页面的第几列数据
#    print(cols)
    del cols[0]                    #清除第一行无用信息
#    print(cols1)

    #for i in range(0):            #去除无用分数
        #del cols3[0]


    cols=qukong(cols)
#    print("qukong")
#    print(cols1)
    #cols1=[int(x) for x in cols1]   #将小数点 变成整数int格式
    #cols2=[int(x) for x in cols2]
    #cols3=[int(x) for x in cols3]
    return(cols)
if __name__ == "__main__":
#输出Excel文件中的第三页，第一列数据
    print(read_excel(3,1))

