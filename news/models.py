from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
    