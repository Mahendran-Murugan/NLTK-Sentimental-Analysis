import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt', encoding='utf-8').read()
textLower = text.lower()
cleanText = textLower.translate(str.maketrans("", "", string.punctuation))


def analyzeSentiment(sentimentText):
    score = SentimentIntensityAnalyzer().polarity_scores(sentimentText)
    print(score)


analyzeSentiment(cleanText)