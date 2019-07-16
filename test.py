import numpy as np
import xlrd as excel
import random

chinese_list='富强民主文明和谐'
ex = excel.open_workbook(r'F:\150\脱敏测试.xlsx')
sheet_list=ex.sheet_names()

page = ex.sheet_by_name('Sheet1')

column1 = page.col_values(3)

title = column1[:1]
data = column1[1:]

def input_list(data):
    datades =[]
    length = len(data)
    for i in range(0,length):
        str = []
        str = data[i]
        for j in range(0,len(str)):
            r_value = random.choice(chinese_list)
            str = str.replace(str[j],r_value,1)
        str = ''.join(str)
        datades.append(str)
        np.asarray(datades)
    return datades

test3 = input_list(data)

print(type(test3))