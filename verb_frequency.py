from collections import Counter
import openpyxl
import xlrd
import re
from xlutils.copy import copy as xl_copy

excel_path = input("excel路径: ")
sheet_index = input("sheet序号: ")
wc_col = input("统计列: ")

data = xlrd.open_workbook(excel_path)
table = data.sheet_by_index(int(sheet_index) - 1)
speech = []
for row in range(table.nrows):
    value = re.sub(r'!|@|#|$|%|^|&|\*|\(|\)|[|]|{|}|"|,|\?|\.|\'|-|_|\d|:|？|；|，|。', " ",
                   table.cell(row, int(wc_col) - 1).value.lower())
    speech.extend(value.split())

wd = Counter(speech)

wc_data = xl_copy(data)
wc_sheet = wc_data.add_sheet('词频统计')
wc_sheet.write(0, 0, "单词")
wc_sheet.write(0, 1, "频率")
item_size = wd.items()

i = 1
for key, value in sorted(wd.items(), key=lambda kv: (kv[0], kv[1])):
    wc_sheet.write(i, 0, key)
    wc_sheet.write(i, 1, value)
    i = i + 1

wc_data.save(excel_path)
input("统计完成，按enter退出！")
