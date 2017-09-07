#!/usr/bin/python3

'''
   date:20170826
   Athor:冉冉
'''

import xlrd
def read_excel():
    # 打开excel文件
    fname = xlrd.open_workbook('test.xls')

    # 获取sheet的名称
    sheet1 = fname.sheet_by_index(0)  # 通过索引获取
    # sheet1 = fname.sheet_by_index()[0]  # 通过索引获取
    # sheet1 = fname.sheet_by_name('sample') # 通过表名获取
    print(sheet1.name)

    # 获取sheet表行数和列数
    print(sheet1.nrows)
    print(sheet1.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(0)  # 获取第1行的内容
    cols = sheet1.col_values(0)  # 获取第1列的内容
    print(rows)
    print(cols)

    # 获取单元格内容
    print(sheet1.cell(1, 0).value)
    print(sheet1.cell_value(1, 0))
    print(sheet1.row(1)[0].value)
    print(sheet1.cell(1, 9).value)

    # 获取单元格的数据类型
    print(sheet1.cell(1, 0).ctype)
    print(sheet1.cell(2, 0).ctype)
    print(sheet1.cell(1, 9).ctype)


if __name__== '__main__':
    read_excel()

