import nltk
from nltk.tokenize import word_tokenize
from .newsmining import getNews
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def getDataToView(search):
    data = []

    news_data = getNews(search)
    analyzer = SentimentIntensityAnalyzer()
    for x in news_data['articles']:
        snt = analyzer.polarity_scores(x['description'])
        data.append({
            'title': x['title'], 
            'description' : x['description'], 
            'date': x['publishedAt'][:10],
            'source': x['source']['name'], 
            'positive': snt['pos'], 
            'neutral' : snt['neu'], 
            'negative': snt['neg']
        })

    return data

