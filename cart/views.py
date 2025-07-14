from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Cart
from main.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
class CartView(TemplateView):
    template_name = 'cart/cart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Корзина'
        context['carts'] = Cart.objects.filter(user=self.request.user)
        # context['total_sum'] = 0
        # context['total_quantity'] = 0
        # for cart in context['carts']:
        #     context['total_sum'] += cart.sum()
        #     context['total_quantity'] += cart.quantity
        return context
    
@login_required(login_url='/login/')
def cart_add(request, products_id):
    product = get_object_or_404(Product, id=products_id)
    cart = Cart.objects.filter(user=request.user, product=product)
    
    if not cart.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = cart.first()
        cart.quantity += 1
        cart.save()
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return redirect(request.META["HTTP_REFERER"])