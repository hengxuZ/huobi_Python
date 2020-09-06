# encoding: utf-8
import xlrd,os,xlwt
from xlutils.copy import copy
workbook = xlrd.open_workbook(os.getcwd()+"/quantify/transaction_log/record.xlsx")

buy_table = workbook.sheet_by_name("buy")

row =buy_table.nrows
col =buy_table.ncols
print(row)
print(col)
# def record_buy_order(dict):
# for index in col:
#     buy_table.c    

new_workbook = copy(workbook)