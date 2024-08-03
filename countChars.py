import os

basePath = "./Output/Muslim/"

sumChars = 0
for bookNum in range(1, 57):
    filePath = os.path.join(basePath, str(bookNum) + ".txt")
    f = open(filePath, "r", encoding="utf-8")
    allData = f.read()
    sumChars += len(allData)
    f.close()

print(sumChars)