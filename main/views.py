from django.shortcuts import render
from .models import Category, Product, Subcategory
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView
from cart.forms import CartAddProductForm


# Create your views here.
class IndexView(TemplateView):
    """ Главная страница """
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'is_popular_products': Product.objects.filter(is_popular_product=True),
            'is_hero_products': Product.objects.filter(is_hero_product=True),
            'subcategories': Subcategory.objects.filter(is_popular_subcategory=True),
            'title': 'Главная'
        })
        return context
    
class ProductDetailView(DetailView):
    """ Страница товара """
    model = Product
    template_name = 'main/product_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['cart_product_form'] = CartAddProductForm()
        return context
    

class CategoriesView(ListView):
    " вывод всех категорий "
    model = Category
    template_name = 'main/categories.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context
    

class SubcategoryView(ListView):
    """ Вывод подкатегорий по категории """
    template_name = 'main/subcategories.html'
    context_object_name = 'subcategories'
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.subcategories.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['title'] = category.title
        return context

    

class ProductListView(ListView):
    """ Список товаров для конкретной категории """
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        """ Возвращаем все товары этой подкатегории """
        subcategory = get_object_or_404(Subcategory, slug = self.kwargs['slug'])
        return subcategory.products.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем подкатегорию для заголовка
        subcategory = get_object_or_404(Subcategory, slug=self.kwargs['slug'])
        context['title'] = subcategory.title  # Заголовок = название подкатегории
        return context

class SearchResultsView(TemplateView):
    """Результаты поиска"""
    template_name = 'components/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        if query:
            context['result'] = Product.objects.filter(Q(title__icontains=query))[:5]
        else:
            context['result'] = []
        return context

class About_us(TemplateView):
    """ Страница 'О нас' """
    template_name = 'main/about_us.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'О нас'
        return context
    
    
    
    
class ContactsView(TemplateView):
    """ страница контактов """
    template_name = 'main/contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Контакты'
        return context
    
    
class BrandsView(TemplateView):
    """ Страница брэндов  """
    template_name = 'main/brands.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Производители'
        return context
    
    
class AgreementView(TemplateView):
    """ Страница пользовательского соглашения """
    template_name = 'main/agreement.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Пользовательского соглашение'
        return context
    