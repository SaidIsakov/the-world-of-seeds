from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'quantity-input',
            'min': '1',
        }),
        label='Количество'
    )
    
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
