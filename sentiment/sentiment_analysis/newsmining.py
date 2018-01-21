import requests
import json
from .keys import newsapi
import datetime as DT

def getNews(news):
    today = DT.date.today()
    week_ago = today - DT.timedelta(days = 7)
    response = requests.get("https://newsapi.org/v2/everything?q="+news+"&from="+str(week_ago)+"&to="+str(today)+"&language=en&apiKey=" + newsapi)
    response_data = response.json()
    return response_data