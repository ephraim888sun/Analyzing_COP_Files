# importing required modules
import re
import PyPDF2
from openpyxl import load_workbook
import os
from methods import follow, comment, frac_Date, open_hole

# def follow(x, lis):
#     if (x in lis):
#         y = lis.index(x)
#         return lis[y + 1]
#     else:
#         return "Not in list"
#
#
# def comment(y, test1, boo):
#     newstr = " "
#     for x in y:
#         if (test1.find(x) != -1):
#             count = test1.count(x)
#             i = 0
#             while (i < count):
#                 i += 1
#                 indx = test1.find(x)
#                 if (indx == -1):
#                     break
#                 test2 = test1[indx:]
#                 if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
#                     m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
#                     z = test2.index(m) + len(m)
#                     newstr += test2[:z] + " "
#                     test1 = test1[0:indx] + test1[indx + z:]
#     return newstr
#
#
# def frac_Date(y, test1, boo):
#     fracstr = " "
#     for x in y:
#         if (test1.find(x) != -1):
#             count = test1.count(x)
#             i = 0
#             while (i < count):
#                 i += 1
#                 indx = test1.find(x)
#                 if (indx == -1):
#                     break
#                 test2 = test1[indx:]
#                 if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
#                     m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
#                     z = test2.index(m) + len(m)
#                     fracstr += m + " "
#                     test1 = test1[0:indx] + test1[indx + z:]
#     return fracstr
#
# def open_hole(y, test1, boo):
#     openstr = " "
#     for x in y:
#         if (test1.find(x) != -1):
#             count = test1.count(x)
#             i = 0
#             while (i < count):
#                 i += 1
#                 indx = test1.find(x)
#                 if (indx == -1):
#                     break
#                 test2 = test1[indx +len(x):]
#                 test3 = test1[indx + len(x)+ 1:]
#                 #print(test3)
#                 for j in test3:
#                     if(j == ";"):
#                         getindex = test3.find(j)
#                         #print(getindex)
#                 if len(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)) != 0:
#                     m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", test2)[0]
#                     z = test2.index(m) + len(m)
#                     openstr += test2[1:1 + getindex] + " "
#                     #print(openstr)
#                     test1 = test1[0:indx] + test1[indx + z:]
#     return openstr

wb = load_workbook(filename=r"")
ws = wb.active

rootdir = r'C:\Users\Ephraim.Sun\Desktop\proj2\test1'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith("CURRENT SCHEMATIC.pdf"):
            pdfFileObj = os.path.join(subdir, file)
            #pdfFileObj = open(r'C:\Users\Ephraim.Sun\Desktop\proj2\test1\AGATE A 1\AGATE A 1 - CURRENT SCHEMATIC.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # print(pdfReader.numPages) # will give total number of pages in pdf

            # extract all texts from page1
            pageObj = pdfReader.getPage(0)
            page_content = pageObj.extractText()

            """get a list from the pdf"""
            list = page_content.splitlines()
            # print(list)

            API = follow('API / UWI', list)

            """take the contents from list and put the good stuff into list_content"""
            if ('al)' in list):
                start = list.index("al)", )
            # else: #Bruh
            #     break
            if ('District' in list):
                end = list.index("District")
            elif ('0District' in list):
                end = list.index("0District")
            # else: #Bruh
            #     break
            # list_content = []
            list_content = list[start + 1:end]
            # print(list_content)

            """Make all list_content into one big string test"""
            test = ''
            for i in list_content:
                x = i
                test = test + x
            # print(test)

            new_str = ''
            test1 = test
            boo = 'False'
            keywords = ["Hydraulic Fracture", "Hydraulic Frac", "Sand Frac", "Hydrl Frac-Acid Base", "Hydrl Frac",
                        "Acid Frac", "Fracture", "Frac"]

            new_str = comment(keywords, test1, boo)
            frac_time = frac_Date(keywords, test1, boo)
            frac_openhole = open_hole(keywords, test1, boo)

            # print(boo)
            row_cell = ' '
            cell_Date = ' '
            cell_fracDate = ' '
            cell_openhole = ' '

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value == API:
                        row_cell = cell.row
            # print(row_cell)

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value == 'Comments':
                        cell_Date = cell.coordinate

            # print(cell_Date)
            if (row_cell != ' ' and cell_Date != ' '):
                # print(type(row_cell))
                # print(type(cell_Date))
                cell_col = cell_Date.rstrip(cell_Date[1])
                # print(cell_col)
                coordinates = str(cell_col) + str(row_cell)
                # print(coordinates)
                ws[coordinates] = new_str
                # print(DATE)

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value == 'Frac Date':
                        cell_fracDate = cell.coordinate

            # print(cell_Date)
            if (row_cell != ' ' and cell_fracDate != ' '):
                # print(type(row_cell))
                # print(type(cell_Date))
                cell_col1 = cell_fracDate.rstrip(cell_fracDate[1])
                # print(cell_col)
                coordinates1 = str(cell_col1) + str(row_cell)
                # print(coordinates)
                ws[coordinates1] = frac_time
                # print(DATE)

            for row in ws.iter_rows():
                for cell in row:
                    if cell.value == 'Open Hole Feet':
                        cell_openhole = cell.coordinate

            # print(cell_Date)
            if (row_cell != ' ' and cell_openhole != ' '):
                # print(type(row_cell))
                # print(type(cell_Date))
                cell_col2 = cell_openhole.rstrip(cell_openhole[1])
                # print(cell_col)
                coordinates2 = str(cell_col2) + str(row_cell)
                # print(coordinates)
                ws[coordinates2] = frac_openhole
                # print(DATE)

wb.save(filename=r'')