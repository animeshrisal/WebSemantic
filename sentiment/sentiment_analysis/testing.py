import nltk
from nltk.tokenize import word_tokenize
from newsmining import getNews
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def getDataToView(search):
    data = []

    news_data = getNews(search)
    analyzer = SentimentIntensityAnalyzer()
    for x in news_data['articles']:
        data.append({
            'source': x['source']['name'], 
        })

    return data

print(getDataToView("trump"))
