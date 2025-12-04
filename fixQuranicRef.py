import re
import os

def readTextFromFile(path):   
    f = open(path, "r", encoding="utf-8")
    allData = f.readlines()
    f.close()
    return("".join(allData))

def saveTextToFile(text, filePath):
    f = open(filePath, "w", encoding="utf-8")
    f.write(text)
    f.close()

def fixQuranicReferencesForSingleAyah(text):
    # Define the regex pattern to match "(<number1>.<number2>)"
    pattern = r"\((\d+)\.(\d+)\)"
    
    # Define the replacement function
    def replacement(match):
        number1 = match.group(1)
        number2 = match.group(2)
        return f"(Surah {number1}: Ayah {number2})"
    
    # Use re.sub() to replace the matched patterns with the desired format
    converted_text = re.sub(pattern, replacement, text)
    
    return converted_text


def fixQuranicReferencesForMultipleAyat(text):
    # Regular expression to match the pattern (number.number-number)
    pattern = r'\((\d+)\.(\d+-\d+)\)'
    
    # Function to replace the matched pattern with the desired format
    def replace_match(match):
        surah = match.group(1)
        ayat = match.group(2)
        return f"(Surah {surah}: Ayat {ayat})"
    
    # Using re.sub to replace all occurrences of the pattern in the text
    converted_text = re.sub(pattern, replace_match, text)
    return converted_text

def fixQuranicReferences(text):
    convertedText = fixQuranicReferencesForSingleAyah(text)
    convertedText = fixQuranicReferencesForMultipleAyat(convertedText)
    return convertedText

# Example text
for partNum in range(7, 17):
    path = os.path.join(".", "Output", "Bukhari", "65p" + str(partNum) + ".txt")
    text = readTextFromFile(path)

    # Convert the text and print the result
    converted_text = fixQuranicReferences(text)
    saveTextToFile(converted_text, path)
