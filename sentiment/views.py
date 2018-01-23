from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .sentiment_analysis.analysis import getDataToView
from .models import news
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

# Create your views here.
@csrf_exempt
def index(request):
    if request.is_ajax():
        print(request.POST['search'])
        news.objects.all().delete()
        try:
            NewsData = getDataToView(request.POST['search'])
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

            return JsonResponse({'insert': 'success'})
        
        except:
            pass

    return render(request, 'index.html')

@csrf_exempt
def chart(request):
    return render(request, 'chart.html')
