from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True,related_name='subcategories')
    popular_category = models.BooleanField()
    
    def get_absolute_url(self):
        pass
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'Категория: pk={self.pk}, title:={self.title}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    manufacturer = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    discription = models.TextField(max_length=5000, null=True, blank=True)
    additional_information = models.TextField(max_length=1000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
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