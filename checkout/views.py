from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
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
    DELIVERY = settings.STANDARD_DELIVERY_CHARGE
    order_form = OrderForm()

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))
    
    line_items = []
    total = 0
    for colour_id, item_data in basket.items():
        colour = get_object_or_404(Colour, pk=colour_id)
        product  = get_object_or_404(Product, pk=colour.product.id)
        name = product.product_name + ' - ' + colour.colour
        image = product.image_url
        price = product.price
        total += item_data * product.price
        product_count = item_data
        line_items.append(
           {'price_data': {
                'currency': STRIPE_CURRENCY,
                'product_data': {
                    'name': name,
                    'images': [image],
                },
                'unit_amount': int(price*100),
            },
        'quantity': item_data,
        })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        line_items.append(
            {'price_data': {
                    'currency': STRIPE_CURRENCY,
                    'product_data': {
                        'name': 'Delivery',
                    },
                    'unit_amount': int(DELIVERY*100),
            },
        'quantity': 1,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('view_basket')) +'?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('checkout')),
    )

    context = {
        'session_id' : session.id,
        'stripe_public_key' : STRIPE_PUBLISHABLE,
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context,)




