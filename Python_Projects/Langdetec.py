from langdetect import detect

text="wellcome to indiA"
language = detect(text)
print("Detected language:",language)