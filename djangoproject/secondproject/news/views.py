from django.shortcuts import render
from news.models import News

# Create your views here.
def news(request):
    newsDataAll = News.objects.all()
    print(newsDataAll)
    return render(request,"news.html",{'newsDetaAll': newsDataAll})

def newsDetail(request,newsid):
    newsData = News.objects.get(id=newsid)
    # print(newsid)
    return render(request,"newsDetail.html",{'keynews': newsData})