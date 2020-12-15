from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .forms import OrderForm
from products.models import Product, Colour
import stripe





def checkout(request):
    basket = request.session.get('basket', {})
    stripe.api_key = settings.STRIPE_SECRET
    STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE
    STRIPE_SUCCESS_URL = settings.STRIPE_SUCCESS_URL 
    STRIPE_CANCEL_URL = settings.STRIPE_CANCEL_URL
    STRIPE_CURRENCY = settings.STRIPE_CURRENCY

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
        'price_data': {
            'currency': STRIPE_CURRENCY,
            'product_data': {
            'name': 'T-shirt',
            },
            'unit_amount': 4000,
        },
        'quantity': 2,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('view_basket')) +'?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('checkout')),
    )

    order_form = OrderForm()
    context = {
        'session_id' : session.id,
        'stripe_public_key' : STRIPE_PUBLISHABLE,
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context,)

  
    """
    return JsonResponse({
        'session_id' : session.id,
        'stripe_secret_key' : stripe.api_key,
    })
    """



