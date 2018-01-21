from django.shortcuts import render
from sentiment.sentiment_analysis.tweetmining import getHashTagTweets
from .models import tweets
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chart(request):
    tweets.objects.all().delete()
    #print(request.POST["hash"])
    
    for x in getHashTagTweets(request.POST["hash"]):
        tweet = tweets()
        tweet.tweets = x.text
        tweet.date = x.created_at
        tweet.save()
    tweet = tweets.objects.all()

    return render(request, 'chart.html', {'tweets': tweet})
