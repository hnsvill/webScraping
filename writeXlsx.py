import xlsxwriter


def writeXL(itmText, iCol, iRow):
    workbook = xlsxwriter.Workbook("C:/Users/Hannah/Desktop/saveInfo.xlsx")
    worksheet = workbook.worksheets("Sheet1")
    # Desktop
    worksheet.write(letterCol(iCol) & iRow, itmText)

    workbook.close()

    print ("Desktop Success!")

import math

alphaSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def letterCol(colNum):
    alphaCol = ""
    while math.floor(colNum/26) >= 26:
        alphaCol = alphaCol + alphaSoup[(colNum % 26) + 1]
        print(alphaCol)
        colNum = colNum - 26
    
    return alphaCol

print(letterCol(100))