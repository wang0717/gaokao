#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd #读取excel文件
import xlwt #写入excel文件
from xlutils.copy import copy #写入excel文件
 # 打开想要更改的excel文件  
old_excel = xlrd.open_workbook(r'B:\2020.xls', formatting_info=True)

# 将操作文件对象拷贝，变成可写的workbook对象  
new_excel = copy(old_excel)

#读取第 个sheet文件
ws = new_excel.get_sheet(0)

#写入excel的第行，第列，某数据
ws.write(2,3,4)

q=15
#重新保存为新excel
new_excel.save('B:\%s.xls'%q)


