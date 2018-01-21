import nltk
from nltk.tokenize import word_tokenize
from newsmining import getNews
from nltk.sentiment.vader import SentimentIntensityAnalyzer 


news_data = getNews("trump")

analyzer = SentimentIntensityAnalyzer()

for x in news_data:
    for x in news_data['articles']:
        print(x['description'], ' ', x['publishedAt'])
        snt = analyzer.polarity_scores(x['description'])
        print(snt)