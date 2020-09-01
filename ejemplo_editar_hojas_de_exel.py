import openpyxl
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('sheet')
sheet[ = 42]
sheet[ = 'hello']
wb.save('path de ejemplo')
sheet2 = wb.create_sheet()
wb.get_sheet_names()
sheet2.title = 'ejemplo'
wb.sabe('path ejemplo')
wb.creat_sheet(index=2, title= 'my other sheet')
wb.save('path ejemplo')
