import re
import PyPDF2
from openpyxl import load_workbook
import os
from methods import follow, casing, getName

# def follow(x, lis):
#     if (x in lis):
#         y = lis.index(x)
#         return lis[y + 1]
#     else:
#         return "Not in list"
#
# def casing(y, test1):
#     newstr = " "
#     for x in y:
#         # if (test1.find(x) != -1):
#         #     newstr += x + " "
#         if (test1.find(x) != -1) and (x == "Open Hole"):
#             count = test1.count(x)
#             i = 0
#             while (i < count):
#                 i += 1
#                 indx = test1.find(x)
#                 if(indx == -1 ):
#                     break
#                 test2 = test1[indx:]
#                 m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
#                 z = test2.index(m) + len(m)
#                 newstr += test2[:z] + " "
#                 test1 = test1[0:indx] + test1[indx + z:]
#     return newstr
#
# def getName(str_list):
#     end = str_list.find("Report Printed")
#     new_str = str_list[9:end]
#     return new_str

count = 2
none_list = []
API_list = []

wb1 = load_workbook(filename=r"")
ws1 = wb1.active
rootdir = r'C:\Users\Ephraim.Sun\Desktop\proj2\test1'


for col in ws1['B']:
    API_list.append(col.value)
API_list.pop(0)
API_list.pop(0)
print(API_list)

wb1.save(filename=r'C:\Users\Ephraim.Sun\Desktop\proj2\findtesthelp.xlsx')


wb = load_workbook(filename=r"C:\Users\Ephraim.Sun\Desktop\proj2\find.xlsx")
ws = wb.active

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith("CURRENT SCHEMATIC.pdf"):
            pdfFileObj = os.path.join(subdir, file)
            #pdfFileObj = open(r'C:\Users\Ephraim.Sun\Desktop\proj2\test1\ABADAN 1T\ABADAN 1T - CURRENT SCHEMATIC.pdf', 'rb')
            #pdfFileObj = open(r'C:\Users\Ephraim.Sun\Desktop\proj2\test1\ALEXANDER D 4\ALEXANDER D 4 - CURRENT SCHEMATIC.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            #print(pdfReader.numPages) # will give total number of pages in pdf

            #extract all texts from page1
            pageObj = pdfReader.getPage(0)
            page_content = pageObj.extractText()

            """get a list from the pdf"""
            list = page_content.splitlines()
            #print(list)

            API = follow('API / UWI', list)

            """Make all list into one big string test"""
            test = ''
            for i in list:
                x = i
                test = test + x
            #print(test)

            name = getName(test)
            #print(name)

            ifbreak = "False"
            for x in API_list:
                if x == API:
                    API_list.remove(x)
                    ifbreak = "True"
                if x == None:
                    none_list.append(name)


            if(ifbreak != "True"):
                coordinates = 'A' + str(count)
                ws[coordinates] = name
                coordinates_API = "B" + str(count)
                ws[coordinates_API] = API
                count += 1

            # if ifbreak !="True":
print(none_list)
print(API_list)

wb.save(filename=r'')
#         cell_API = ' '
#         cell_Name = ' '
#
#         for row in ws.iter_rows():
#             for cell in row:
#                 if cell.value == "API":
#                     cell_API = cell.coordinate
#         print(cell_API)
#
#         for row in ws.iter_rows():
#             for cell in row:
#                 if cell.value == 'Name':
#                     cell_Name = cell.coordinate
#         print(cell_Name)
#
#         if (cell_Name != ' ' and cell_API != ' '):
#             # print(type(row_cell))
#             # print(type(cell_Name))
#             cell_col = cell_Name.rstrip(cell_Name[1])
#             print(cell_col)
#             coordinates = str(cell_col) + str(count)
#             print(coordinates)
#             ws[coordinates] = name
#             cell_col1 = cell_API.rstrip(cell_API[1])
#             print(cell_col1)
#             coordinates_API = str(cell_col1) + str(count)
#             print(coordinates_API)
#             ws[coordinates_API] = API
#             count += 1
#             # print(DATE)