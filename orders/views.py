from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order, OrderItem
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from main.models import Product
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


@login_required(login_url='/user/login')
def create_order(request):
    cart = Cart(request)
    total_price = sum(item['total_price'] for item in cart)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                user = request.user,
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                phon_num = form.cleaned_data.get('phon_num'),
                city = form.cleaned_data.get('city'),
                postal_code = form.cleaned_data.get('postal_code'),
                delivered_address = form.cleaned_data.get('postal_code'),
            )
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    total_price=item['total_price'],
                )
            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[
                        {
                        'price_data':{
                                'currency':'usd',
                                'product_data':{
                                    'name': item['item'].name,
                                },
                                'unit_amount': int(item['total_price'] * 100),
                            },
                            'quantity':item['quantity'],
                        } for item in cart
                    ],
                    mode='payment',
                    success_url='http://localhost:8000/orders/completed',
                    cancel_url='http://localhost:8000/orders/create-order',
                )
                
                return redirect(session.url, code=303)
            except Exception as e:
                return render(request, 'orders/create_orders', {
                    'form':form,
                    'cart':cart,
                    'error':str(e)
                })
    
    form = OrderForm(initial={
        'first_name':request.user.first_name,
        'last_name':request.user.last_name,
        'email':request.user.email,
        'phon_num':request.user.phon_num,
        'postal_code':request.user.postal_code,
        'delivered_address':request.user.delivered_address,
        'city':request.user.city,
    })
    
    return render(request, 'orders/create_orders.html', {
        'form':form,
        'cart':cart,
        'total_price':total_price,
        
    })
    
@login_required(login_url='/user/login')
def order_success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'orders/order_succsess.html')
    