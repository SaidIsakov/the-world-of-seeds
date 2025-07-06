from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Введите пожалуйста свою почту')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser должен иметь is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
        
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phon_num = PhoneNumberField(unique=True,verbose_name='Номер телефона', region='RU')
    email = models.EmailField(unique=True,verbose_name='Email', max_length=254)
    first_name = models.CharField(max_length=150,verbose_name='Имя')
    password = models.CharField(max_length=128,verbose_name='Пароль')
    last_name = models.CharField(max_length=150,verbose_name='Фамилия')
    is_active = models.BooleanField(default=True,verbose_name='Активен')
    is_staff = models.BooleanField(default=False,verbose_name='Администратор?')
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return str(self.phon_num)