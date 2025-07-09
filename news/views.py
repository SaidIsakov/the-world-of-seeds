from django.shortcuts import render
from .models import New
from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import get_object_or_404
# Create your views here.



class NewsView(ListView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Новости'
        return context
    
