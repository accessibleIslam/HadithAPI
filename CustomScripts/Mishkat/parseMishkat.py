import json
import os

input_file = os.path.join(".", "JSONFiles", "Mishkat", "mishkat_almasabih.json")
output_root = os.path.join(".", "Output", "Mishkat")

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

def extract_english_hadiths(data):
    hadithDict = {}
    for hadith in data:
        hadithId = hadith["id"]
        hadithIdInBook = hadith["idInBook"]
        chapterId = hadith["chapterId"]
        englishText = hadith["english"]["narrator"] + " " + hadith["english"]["text"]
        
        if chapterId not in hadithDict:
            hadithDict[chapterId] = {}
        hadithDict[chapterId][hadithIdInBook] = englishText
    return(hadithDict)

hadiths = extract_english_hadiths(data["hadiths"])

for chapter, contents in hadiths.items():
    output_file_path = os.path.join(output_root, f"{chapter}.txt")
    output_text = ""
    for hadithNumber, hadithText in contents.items():
        output_text += f"Hadith - {hadithNumber}\n"
        output_text += hadithText.replace('\n\n', '\n').strip() + "\n"
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(output_text)