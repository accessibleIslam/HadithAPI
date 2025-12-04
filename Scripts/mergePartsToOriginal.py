import os

def mergeAllParts(rootFolder, originalFileIdentifier):
    partNumber = 1
    originalFilePath = os.path.join(rootFolder, originalFileIdentifier + ".txt")
    partFilePath = os.path.join(rootFolder, originalFileIdentifier + "p" + str(partNumber) + ".txt")

    if not os.path.exists(partFilePath):
        return
    with open(originalFilePath, 'w', newline='\n') as original:
        while os.path.exists(partFilePath):
            print(f"Writing {partFilePath} to {originalFilePath}")
            with open(partFilePath, 'r', newline='\n') as partFile:
                content = partFile.read()
                if partNumber > 1:
                    content = "\n" + content
                original.write(content)
            partNumber += 1
            partFilePath = os.path.join(rootFolder, originalFileIdentifier + "p" + str(partNumber) + ".txt")

rootFolder = os.path.join(".", "Output", "Bukhari")

for i in range(1, 98):
    fileIdentifier = str(i)
    mergeAllParts(rootFolder, fileIdentifier)
