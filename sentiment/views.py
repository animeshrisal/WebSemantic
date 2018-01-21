from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def chart(request):

    return render(request, 'chart.html', {'tweets': tweet})
