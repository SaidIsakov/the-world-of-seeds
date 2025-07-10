from django.urls import path
from .views import*

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories', CategoriesView.as_view(), name='get_categories'),
    path('subcategories/<slug:slug>/', SubcategoryView.as_view(), name='get_subcategories'),
    path('product/<slug:slug>/', ProductListView.as_view(), name='get_products_list'),
    path('about-us/', About_us.as_view(), name='about_us'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('brands/', BrandsView.as_view(), name='brands'),
    path('agreement/', AgreementView.as_view(), name='agreement'),
    
]
