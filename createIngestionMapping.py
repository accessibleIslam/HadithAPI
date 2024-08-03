import os

def readColumnName(textLine):
    columnName = textLine.split(':')[0].strip()
    columnName.strip()
    return columnName

def createIngestionTextPart(columnName):
    ingestiontext = '{"column":"'+ columnName +'","path":"$.' + columnName + '","datatype":""}'
    return ingestiontext

f = open(os.path.join("./testFile.txt"), "r", encoding="utf-8")

textLines = f.readlines()
fullOutput = "["

for textLine in textLines:
    columnName = readColumnName(textLine)
    ingestionTextPart = createIngestionTextPart(columnName)
    fullOutput += ingestionTextPart + ", "
    # print(columnName)
    # print(ingestionTextPart)

fullOutput = fullOutput[:-2] + "]"

print(fullOutput)
f.close()