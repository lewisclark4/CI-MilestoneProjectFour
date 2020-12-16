from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from products.models import Product, Colour
import stripe


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": stripe_secret_key,
    }

    return render(request, 'checkout/checkout.html', context)

