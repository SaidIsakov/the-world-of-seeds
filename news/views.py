from django.shortcuts import render
from .models import New
# Create your views here.

def News(request):
    news = New.objects.all()
    
    context = {
        'title':'Новости',
        'news': news
    }
    
    return render(request, 'main/news.html', context)