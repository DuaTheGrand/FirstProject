import openpyxl
from openpyxl import Workbook
wb = openpyxl.reader.excel.load_workbook(filename="sheet.xlsx", keep_links=True)
wb.active = 0
sheet = wb.active
print("Расписание " + "на " + sheet['A13'].value)
print("")
# print(sheet['A13'].value)

for i in range(13, 18):
    print(sheet['C' + str(i)].value)
    print(sheet['G' + str(i)].value)
