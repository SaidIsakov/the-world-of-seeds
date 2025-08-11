from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phon_num', 'email', 'first_name',
                  'last_name', 'city', 
                  'adress1', 'postal_code']