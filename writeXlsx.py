import xlsxwriter

workbook = xlsxwriter.Workbook("C:/Users/Hannah/Desktop/helloDesktop.xlsx")
worksheet = workbook.worksheets("Sheet1")
# Desktop
worksheet.write("A1", "Hello, Python")

workbook.close()

print ("Desktop Success!")