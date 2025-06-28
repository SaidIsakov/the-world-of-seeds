from django.contrib import admin
from .models import New
# Register your models here.

@admin.register(New)
class NewAdminClass(admin.ModelAdmin):
    pass
