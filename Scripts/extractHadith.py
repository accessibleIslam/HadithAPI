import json
import os

def createFolderIfNotExists(path):
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
        return

def saveTextToFile(text, filePath):
    f = open(filePath, "a", encoding="utf-8")
    f.write(text)
    f.close()

def saveHadithToFile(collectionName, bookNumber, hadithNumber, hadithText):
    if bookNumber == 0:
         print(hadithNumber, hadithText)
    outputFolderPath = os.path.join("Output", collectionName)
    createFolderIfNotExists(outputFolderPath)
    outputFilePath = os.path.join(outputFolderPath, str(bookNumber) + ".txt")
    text = "Hadith - " + str(hadithNumber) + "\n" + hadithText
    if text[-1] not in ('.', '!', '?'):
        text += '.'
    text += "\n"
    saveTextToFile(text, outputFilePath)

collectionName = "Muslim"
jsonFileName = "eng-muslim.json"
f = open(os.path.join("./JSONFiles", jsonFileName), "r", encoding="utf-8")
allData = json.load(f)
f.close()
totalAhadith = len(allData["hadiths"])

ahadith = allData["hadiths"]

ahadithDict = {}
maxBookNumber = 0
lastBookHadithNumber = 0
for i in range(totalAhadith):
    hadithNumber = ahadith[i]["hadithnumber"]
    hadithText = ahadith[i]["text"]
    hadithBookNumber = ahadith[i]["reference"]["book"]
    hadithInBookNumber = ahadith[i]["reference"]["hadith"]
    if hadithBookNumber == 0:
        hadithBookNumber = maxBookNumber
    else:
        maxBookNumber = hadithBookNumber
    if hadithInBookNumber == 0:
        hadithInBookNumber = lastBookHadithNumber + 1
    else:
        lastBookHadithNumber = hadithInBookNumber
    
    if hadithBookNumber not in ahadithDict.keys():
        ahadithDict[hadithBookNumber] = {}
    ahadithDict[hadithBookNumber][hadithInBookNumber] = hadithText
    saveHadithToFile(collectionName, hadithBookNumber, hadithInBookNumber, hadithText)
