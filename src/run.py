# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：wangziqian2 
@File    ：run.py
@Author  ：Wang
@Date    ：2022/6/20 11:39 上午 
"""
from mysql import sql
from def_paixu import paixu



#将sql查询值转换为list
def sql_list(my_list):
    m_list=[]
    for i in my_list:
        if i[0] != None:
            m_list = m_list + [i[0]]
    return m_list
#获取指定年的文理一分一档数据
def year_list(year):
    sql_li_num = sql_list(sql("select %s_li_num from score"%year))
    sql_li = sql_list(sql("select %s_li from score"%year))
    sql_wen_num = sql_list(sql("select %s_wen_num from score" % year))
    sql_wen = sql_list(sql("select %s_wen from score" % year))

    return (sql_li_num,sql_li,sql_wen_num,sql_wen)
list_2021=year_list(2021)
list_2020=year_list(2020)
print(list_2021[1])
print(list_2020[1])
print(list_2020[0])
list_20=paixu(list_2021[1],list_2020[1],list_2020[0])
print(list_20[0])
print(list_20[1])
print(list_20[2])