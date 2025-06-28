from django.shortcuts import render
from .models import Category, Product, Gallery, Subcategory
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    is_popular_products = Product.objects.filter(is_popular_product=True)
    is_hero_products = Product.objects.filter(is_hero_product=True)
    #categories = Category.objects.all()
    subcategories = Subcategory.objects.filter(is_popular_subcategory=True)
    
    context = {
        'is_popular_products':is_popular_products,
        'is_hero_products': is_hero_products,
        'title':'Главная',
        #'categories':categories,
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
    """ Возращает категории на отдельной странице """
    categories = Category.objects.all()
    
    context = {
        'title': 'Каталог',
        'categories':categories
    }
    return render(request, 'main/categories.html', context)

def get_subcategories(request,slug):
    """ Возращает подкатегории по категории """
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategories.all()
        
    context = {
        'title':category.title,
        'subcategories':subcategories
    }
    return render(request, 'main/subcategories.html', context)

def get_products_list(request, slug):
    """ Выводит на отдельной странице продукты подкатегории """
    subcategory = Subcategory.objects.get(slug=slug)
    products = subcategory.products.all()
    
    context = {
        'title':subcategory.title,
        'products':products
    }
    return render(request, 'main/product_list.html', context)