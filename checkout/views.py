from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from products.models import Product, Colour
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "address_1": request.POST["address_1"],
            "address_2": request.POST["address_2"],
            "city": request.POST["city"],
            "county": request.POST["county"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for colour_id, item_data in basket.items():
                try:
                    colour = get_object_or_404(Colour, pk=colour_id)
                    product  = get_object_or_404(Product, pk=colour.product.id)
                    order_line_item = OrderLineItem(
                        order=order, product=product, colour=colour, quantity=item_data,
                    )
                except Product.DoesNotExist or Colour.DoesNotExist:
                    messages.error(request, (
                        "There was an error processing one of the items in your basket."
                        "Please call for further assistance."),
                    )
                    order.delete()
                    return redirect(reverse("view_basket"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "Your form contains some invalid details."
                "Please double check your information",
            )
    

    else:
    basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        grand_total = current_basket['grand_total']
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=["card"],
        )

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)

