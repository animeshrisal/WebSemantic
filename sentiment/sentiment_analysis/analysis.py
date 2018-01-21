import nltk
from nltk.tokenize import word_tokenize
from newsmining import getNews
from nltk.sentiment.vader import SentimentIntensityAnalyzer 



def getDataToView(search):
    data = []

    news_data = getNews(search)
    analyzer = SentimentIntensityAnalyzer()
    for x in news_data:
        for x in news_data['articles']:
            print(x['description'], ' ', x['publishedAt'])
            snt = analyzer.polarity_scores(x['description'])
            data.append({'title': x['title'], 'description' : x['description'], 'date': x['publishedAt'][:10], 'positive': snt['pos'], 'neutral' : snt['neu'], 'negative': snt['neg']})

    return data

print(getDataToView("obama"))