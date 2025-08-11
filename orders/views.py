from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderForm

def create_order(request):
    
    
    form = OrderForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phon_num': request.user.phon_num,
        'email': request.user.email,
        'city': request.user.city,
        'adress1': request.user.adress1,
        'postal_code': request.user.postal_code,
    })
    cart = Cart(request)
    return render(request, 'orders/create_orders.html', {'cart':cart, 'form':form}) 

def order_success(request):
    return render(request, 'orders/order_succsess.html')