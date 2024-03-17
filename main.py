import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
textLower = text.lower()
cleanText = textLower.translate(str.maketrans("", "", string.punctuation))
tokenizeWords = cleanText.split()
stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
finalWords = []
for i in tokenizeWords:
    if i not in stopWords:
        finalWords.append(i)

emotionList = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clearLine = line.replace('\n', '').replace(',', '').replace('\'', '').strip()
        word, emotion = clearLine.split(':')
        if word in finalWords:
            emotionList.append(emotion)

print(emotionList)
counter = Counter(emotionList)
print(counter)


fig, ax1 = plt.subplots()
ax1.bar(counter.keys(), counter.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()