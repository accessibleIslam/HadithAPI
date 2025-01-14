import os
import re

inputRootFolder = os.path.join(".", "Output", "Bukhari")
outputRootFolder = os.path.join(".", "Output", "BukhariDiff")

def transformToSingleLineAhadith(inputFile):
    with open(inputFile, 'r') as inputFile:
        lines = inputFile.readlines()

    mergedLines = []
    currentHadith = ""

    for line in lines:
        if re.match(r'^Hadith - \d+', line):
            if currentHadith:
                mergedLines.append(currentHadith.strip())
            mergedLines.append(line.strip())
            currentHadith = ""
        else:
            currentHadith += " " + line.strip()

    if currentHadith:
        mergedLines.append(currentHadith.strip())

    return mergedLines

def writeLinesToFile(lines, outputFilePath):
    with open(outputFilePath, 'w') as outputFile:
        for line in lines:
            outputFile.write(line + "\n")

for bookNumber in range(1, 98):
    if bookNumber == 94:
        bookFilePath = os.path.join(inputRootFolder, str(bookNumber) + ".txt")
        outputFilePath = os.path.join(outputRootFolder, str(bookNumber) + ".txt")
        print(f"Proceesing {bookFilePath} to {outputFilePath}")
        mergedAhadith = transformToSingleLineAhadith(bookFilePath)
        writeLinesToFile(mergedAhadith, outputFilePath)