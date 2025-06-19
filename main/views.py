from django.shortcuts import render
from .models import Category, Product, Gallery
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    is_popular_products = Product.objects.filter(is_popular_product=True)
    is_hero_products = Product.objects.filter(is_hero_product=True)
    categories = Category.objects.all()
    subcategories = Category.objects.filter(parent=True)
    
    context = {
        'is_popular_products':is_popular_products,
        'is_hero_products': is_hero_products,
        'title':'Главная',
        'categories':categories,
        'subcategories':subcategories
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

def get_categories(request):
    categories = Category.objects.filter(parent=None)
    
    context = {
        'title': 'Каталог товаров',
        'categories': categories
    }
    
    return render(request, 'main/categories.html', context)