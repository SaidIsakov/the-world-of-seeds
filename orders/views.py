from venv import logger
from django.shortcuts import render,redirect
from cart.cart import Cart
from .forms import OrderForm
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
import yookassa
from yookassa import Payment
import uuid
from yookassa.domain.exceptions import BadRequestError, ForbiddenError, NotFoundError
from django.http import JsonResponse
from django.contrib import messages


# Конфигурация Stripe
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Конфигурация Yookassa
yookassa.Configuration.account_id = settings.YOOKASSA_SHOP_ID
yookassa.Configuration.secret_key = settings.YOOKASSA_SECRET_KEY


@login_required(login_url='/user/login/')
def create_order(request):
    cart = Cart(request)

    # Проверка на пустую корзину
    if not cart:
        return redirect('cart_detail')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                # Создаем заказ в базе данных
                order = Order(
                    user=request.user,
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    phon_num=form.cleaned_data.get('phon_num'),
                    email=form.cleaned_data.get('email'),
                    # city=form.cleaned_data.get('city'),
                    # adress1=form.cleaned_data.get('adress1'),
                    # postal_code=form.cleaned_data.get('postal_code'),
                )
                order.save()

                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        total_price=item['total_price']
                    )

                # Создаем платеж в ЮKassa

                idempotence_key = str(uuid.uuid4())
                payment = Payment.create({
                    "amount": {
                        "value": str(cart.get_total_price()),
                        "currency": "RUB"
                    },
                    "confirmation": {
                        "type": "redirect",
                        "return_url": request.build_absolute_uri(f'/orders/order_success/?order_id={order.id}')
                    },
                    "capture": True,
                    "description": f"Заказ №{order.id}",
                    "metadata": {
                        "order_id": order.id
                    }
                }, idempotence_key)

                # Сохраняем ID платежа в заказе
                order.payment_id = payment.id
                order.save()
                return redirect(payment.confirmation.confirmation_url, code=303)

            except BadRequestError as e:
              logger.error(f"YooKassa BadRequestError: {e}")
              return JsonResponse({
            'status': 'error',
            'message': 'Неверные параметры запроса',
            'details': str(e)
        }, status=400)

            except BadRequestError as e:
                logger.error(f"YooKassa BadRequestError: {e}")
                messages.error(request, f'Ошибка запроса: {str(e)}')
                return render(request, 'orders/create_orders.html', {
                    'form': form,
                    'cart': cart,
                    'error': f"Ошибка запроса: {str(e)}"
                })

            except ForbiddenError as e:
                logger.error(f"YooKassa ForbiddenError: {e}")
                # Очищаем возможные проблемы с сессией
                if 'cart' in request.session:
                    del request.session['cart']

                messages.error(request, 'Ошибка авторизации платежной системы. Проверьте настройки YooKassa.')
                return render(request, 'orders/create_orders.html', {
                    'form': form,
                    'cart': cart,
                    'error': "Ошибка авторизации платежной системы"
                })

            except NotFoundError as e:
                logger.error(f"YooKassa NotFoundError: {e}")
                messages.error(request, 'Платежная система временно недоступна')
                return render(request, 'orders/create_orders.html', {
                    'form': form,
                    'cart': cart,
                    'error': "Платежная система временно недоступна"
                })

            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                messages.error(request, 'Произошла непредвиденная ошибка')
                return render(request, 'orders/create_orders.html', {
                    'form': form,
                    'cart': cart,
                    'error': "Произошла непредвиденная ошибка"
                })



            # except Exception as e:
            #     logger.error(f"YooKassa error: {str(e)}")
            #     return render(request, 'orders/create_orders.html', {
            #         'form': form,
            #         'cart': cart,
            #         'error': "Ошибка обработки платежа. Пожалуйста, попробуйте еще раз.",
            #     })

    # Заполняем форму начальными данными пользователя
    form = OrderForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phon_num': request.user.phon_num,
        'email': request.user.email,
        # 'city': request.user.city,
        # 'adress1': request.user.adress1,
        # 'postal_code': request.user.postal_code,
    })

    return render(request, 'orders/create_orders.html', {
        'form': form,
        'cart': cart,
    })

@login_required(login_url='/users/login/')
def order_success(request):
    order_id = request.GET.get('order_id')

    if order_id:
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.paid = True  # Помечаем заказ как оплаченный
            order.status = 'paid'  # Меняем статус
            order.save()
        except Order.DoesNotExist:
            pass

    # Очищаем корзину
    if 'cart' in request.session:
        cart = Cart(request)
        cart.clear()
        del request.session['cart']

    context = {'order_id': order_id}
    return render(request, 'orders/order_success.html', context)
