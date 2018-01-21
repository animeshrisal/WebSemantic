from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .sentiment_analysis.analysis import getDataToView
from .models import news

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chart(request):
    news.objects.all().delete()
    try:
        NewsData = getDataToView(request.POST['title'])
        for data in NewsData:
            newsObject = news(
                newstitle = data['title'],
                newsdescription = data['description'],
                date = data['date'],
                source = data['source'],
                negative_value = data['negative'],
                neutral_value = data['neutral'],
                positive = data['positive']
            )

            newsObject.save()

        analyzedData = news.objects.all()
        return render(request, 'chart.html', {'analyzedData': analyzedData})

    except:
        return render(request, 'error.html')
