import xlsxwriter

def writeXL(itmText, iCol, iRow):
    workbook = xlsxwriter.Workbook("C:/Users/Hannah/Desktop/helloDesktops.xlsx")
    worksheet = workbook.worksheets("Sheet1")
    # Desktop
    worksheet.write()

    workbook.close()

    print ("Desktop Success!")

def getLetterCol(iCol):
    alphabetSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return print(iCol % 2)

print getLetterCol(5)