from .models import New
from django.views.generic import ListView



class NewsView(ListView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Новости'
        return context
    
