from django import forms
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegistrUser(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        error_messages={'max_length': 'Имя не должно превышать 50 символов.'},
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        error_messages={'max_length': 'Фамилия не должна превышать 50 символов.'},
        widget=forms.TextInput(attrs={'placeholder': 'Введите Фамилию'})
    )
    phon_num = PhoneNumberField(
        error_messages={'invalid': 'Введите корректный номер телефона(должен начинаться с +7).','unique':'Такой номер телефона уже зарегестрирован'},
        widget=forms.TextInput(attrs={
            'placeholder': '+7 (_) _--',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label='Email',
        error_messages={
            'invalid': 'Введите корректный адрес почты.',
            'unique': 'Эта электронная почта уже занята.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Введите адресс электронной почты'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"type": "password"})
    )

    agree_to_terms=forms.BooleanField(
        label='Даю согласие на обработку данных в соответствии с УК РФ',
        required=True,)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'phon_num', 'email', 'password']
        
class LoginUserForm(AuthenticationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
        })
    )
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }