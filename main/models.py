from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_popular_category = models.BooleanField()
    
    def get_absolute_url(self):
        return reverse('get_subcategories', kwargs={'slug':self.slug})
    
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'Категория: pk={self.pk}, title:={self.title}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def get_parent_category_image(self):
        """ Для получения родительской фотки """
        if self.image:
            return self.image.url
        else:
            pass
        
    def get_subcategory_image(self):
        pass
    
class Subcategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='subcategories/')   
    is_popular_subcategory = models.BooleanField()
    slug = models.SlugField(unique=True)
    subcategory_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('get_products_list', kwargs={'slug':self.slug})
    
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
    
class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manufacturer = models.CharField(max_length=50)
    quantity = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discription = models.TextField(max_length=5000, null=True, blank=True)
    additional_information = models.TextField(max_length=1000, null=True, blank=True)
    availability = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    slug = models.SlugField(unique=True, null=True)
    is_popular_product = models.BooleanField()
    is_hero_product = models.BooleanField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})
    
    
    def __repr__(self):
        return f'Товар: pk={self.pk}, title={self.title} price={self.price}'
    
    def get_first_photo(self):
        """ Отображает первую фотографию продукта на index.html """
        if self.images.first():
            return self.images.first().image.url
        
            
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
class Gallery(models.Model):
    image = models.ImageField(upload_to='products/')
    products = models.ForeignKey(Product, on_delete=models.CASCADE,
                                 related_name='images')
    
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'