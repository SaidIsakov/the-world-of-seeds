from django.db import models
from main.models import Product
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Order(models.Model):
    STATUS_CHOICES = [
        ('ponding', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phon_num = models.CharField(unique=True,verbose_name='Номер телефона')
    email = models.EmailField(unique=True,verbose_name='Email', max_length=254)
    first_name = models.CharField(max_length=150,verbose_name='Имя')
    last_name = models.CharField(max_length=150,verbose_name='Фамилия')
    # city = models.CharField(max_length=100)
    # adress1 = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=40, blank=True, default='pending')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    
    def __str__(self):
        return f'Заказ {self.id} | Пользователь {self.email}'
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return f'Товар {self.product} | Заказ {self.order.pk}'
    
    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
        