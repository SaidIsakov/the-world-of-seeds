from django.shortcuts import render
from .models import Category, Product, Gallery
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    is_popular_products = Product.objects.filter(is_popular_product=True)
    is_hero_products = Product.objects.filter(is_hero_product=True)
    
    context = {
        'is_popular_products':is_popular_products,
        'is_hero_products': is_hero_products,
        'title':'Главная',
    }
    
    return render(request, 'main/index.html', context)

def product_detail(request, slug):
    """ Переход на страницу с товаром """
    product = get_object_or_404(Product, slug=slug)
    context = {
        'title':product.title,
        'product':product,
    }
    return render(request, 'main/product_detail.html', context)

