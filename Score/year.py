#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：gaokao 
@File    ：year.py
@Author  ：Wang
@Date    ：2022/6/20 23:38 
@Show    :通过sql语句，查询指定年份的一分一档数据
"""
# 将sql查询值转换为list
from Score.mysql import sql


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
