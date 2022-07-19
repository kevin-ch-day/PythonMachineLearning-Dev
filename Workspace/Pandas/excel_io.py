import pandas as pd

df = pd.read_excel('.\DATA\\my_excel_file.xlsx', sheet_name='First_Sheet')
workBook = pd.ExcelFile('.\DATA\\my_excel_file.xlsx')
print(workBook.sheet_names)

x = pd.read_excel('.\DATA\\my_excel_file.xlsx', sheet_name=None)
print(type(x))

df = x['First_Sheet']
df.to_excel('.\OUTPUT\\exampleExcel.xlsx', index=False)