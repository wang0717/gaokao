# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wangziqian2 
@File    ：run.py
@Author  ：Wang
@Date    ：2022/6/20 11:39 上午 
"""
import xlwt
from mysql import sql
from def_sort import sort


# 将sql查询值转换为list
def sql_list(my_list):
    m_list = []
    for i in my_list:
        if i[0] != None:
            m_list = m_list + [i[0]]
    return m_list


# 获取指定年的文理一分一档数据
def year_list(year):
    sql_li_num = sql_list(sql("select %s_li_num from score" % year))
    sql_li = sql_list(sql("select %s_li from score" % year))
    sql_wen_num = sql_list(sql("select %s_wen_num from score" % year))
    sql_wen = sql_list(sql("select %s_wen from score" % year))

    return sql_li_num, sql_li, sql_wen_num, sql_wen


# 进行排序21转换为20年（21年人数，20年人数，20年分数）
list_20 = sort(year_list(2021)[1], year_list(2020)[1], year_list(2020)[0])
list_21 = sort(year_list(2020)[1], year_list(2021)[1], year_list(2021)[0])
lis = [list_20, list_21]
# print(lis)


# 写入Excel
# 写入几页，这几页数据的list
def excel_write(sheet_num, my_list):
    # 1 新建工作簿
    workbook = xlwt.Workbook()
    # 2 新建工作表并重命名
    for i in range(0, sheet_num):
        worksheet = workbook.add_sheet(str(i))  # 将工作表worksheet命名为
        # 3 写入内容
        print("写入Excel表" + str(i) + "开始")
        long = min(len(my_list[i][0]), len(my_list[i][1]), len(my_list[i][2]))
        t = 0
        while t < long:
            worksheet.write(t + 1, 0, my_list[i][0][t])
            worksheet.write(t + 1, 1, my_list[i][1][t])
            worksheet.write(t + 1, 2, my_list[i][2][t])
            t = t + 1
    # 4 保存
    workbook.save('B:\桌面\qweeeeeee.xls')
    print("写入Excel表结束")


excel_write(2, lis)
