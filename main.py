import re
import PyPDF2
from openpyxl import load_workbook
import os


wb1 = load_workbook(filename=r"C:\Users\Ephraim.Sun\Desktop\proj2\original.xlsx")
ws1 = wb1.active
rootdir = r'C:\Users\Ephraim.Sun\Desktop\proj2\test1'

count = 2
none_list = []
API_list = []
for col in ws1['B']:
    API_list.append(col.value)
API_list.pop(0)
API_list.pop(0)
print(API_list)