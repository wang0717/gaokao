#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd #读取excel文件 加载包python3\Scripts\pip3.exe install xlrd
import xlwt #写入excel文件
from xlutils.copy import copy #写入excel文件
import def_read_excel
import def_paixu
import def_chazhi
import def_write_excel
import def_shuju

read_excel=def_read_excel.read_excel
write_excel=def_write_excel.write_excel
paixu=def_paixu.paixu
chazhi=def_chazhi.chazhi
shuju=def_shuju.shuju

#一年数据
year1=shuju(1)
#print("输入第一年数据：")
#print(year1[0])
#print(year1[1])
#print(year1[2])
#二年数据
year2=shuju(2)
#三年数据
year3=shuju(3)
#四年数据
year4=shuju(4)

year5=shuju(5)

shuju1=paixu(year1[0],year1[1],year1[2])
shuju2=paixu(year2[0],year2[1],year2[2])
shuju3=paixu(year3[0],year3[1],year3[2])
shuju4=paixu(year4[0],year4[1],year4[2])
shuju5=paixu(year5[0],year5[1],year5[2])

write_excel(shuju1,shuju2,shuju3,shuju4,shuju5,22)
print("结束")



