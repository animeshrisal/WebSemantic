from django.shortcuts import render
from sentiment.sentiment_analysis.tweetmining import getHashTagTweets
from .models import tweets

# Create your views here.
def index(request):
    tweets.objects.all().delete()
    for x in getHashTagTweets('obama'):
        tweet = tweets()
        tweet.tweets = x.text
        tweet.date = x.created_at
        tweet.save()

    return render(request, 'index.html')

def chart(request):
    tweet = tweets.objects.all()
    return render(request, 'chart.html', {'tweet': tweet})