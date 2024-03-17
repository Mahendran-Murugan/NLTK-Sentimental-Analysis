import string
text = open('read.txt', encoding='utf-8').read()
textLower = text.lower()
cleanText = textLower.translate(str.maketrans("", "", string.punctuation))
print(cleanText)