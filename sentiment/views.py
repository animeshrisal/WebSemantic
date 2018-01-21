from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import news

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chart(request):
    NewsData = news.objects.all().remove()
    
    return render(request, 'chart.html', {})
