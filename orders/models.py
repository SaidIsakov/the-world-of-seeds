from django.db import models
from main.models import Product
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает оплаты'),
        ('paid', 'Оплачен'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('canceled', 'Отменен'),
        ('failed', 'Ошибка оплаты'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phon_num = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email', max_length=254)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    # city = models.CharField(max_length=100)
    # adress1 = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    tracking_number = models.CharField(max_length=40, blank=True)

    # Важные поля для работы с оплатами
    payment_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='ID платежа')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Общая сумма заказа
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Общая сумма')

    def __str__(self):
        return f'Заказ {self.id} | Пользователь {self.email}'

    def save(self, *args, **kwargs):
        # Автоматически обновляем статус при изменении paid
        if self.paid and self.status == 'pending':
            self.status = 'paid'
        elif not self.paid and self.status == 'paid':
            self.status = 'pending'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Товар {self.product} | Заказ {self.order.pk}'

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
