from django.db import models
from main.models import Product
from users.models import CustomUser

class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self )
    
    def total_quantity(self):
        return sum(cart.quantity for cart in self)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = CartQuerySet.as_manager()
    
    def __str__(self):
        return f'Пользователь {self.user.email} | Продукт {self.product.title} | Количество {self.quantity} '
   
    def sum(self):
        return self.product.price * self.quantity
    
    
