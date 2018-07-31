import xlsxwriter

def writeXL(itmText, iCol, iRow):
    workbook = xlsxwriter.Workbook("C:/Users/Hannah/Desktop/helloDesktops.xlsx")
    worksheet = workbook.worksheets("Sheet1")
    # Desktop
    worksheet.write()

    workbook.close()

    print ("Desktop Success!")