from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from products.models import Product, Colour
from profiles.forms import UserProfileForm, UserForm
from profiles.models import UserProfile
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    This view creates stripe payment intent metadata
    to allow our webhook handler to identify whether
    a user selects to 'save info' when placing an
    order. This then allows us to update the user
    profile where applicable.
    """
    try:
        payment_intent_id = request.POST.get(
                                    'client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
                    request, ('There was an issue processing your payment. '
                              + 'Please try again, '
                              + 'or call us for more assistance.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    This view displays the order form & basket
    so that a user can check their order, add
    their delivery details and checkout.
    User details are prepopulated
    where known.
    When a user posts the form, this view
    will also create a stripe payment intent,
    create the order & order line items.
    The "checkout" boolean is used to identify
    the order progress.
    """

    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_intent_id = request.POST.get(
                                        'client_secret').split('_secret')[0]
            order.stripe_payment_intent_id = payment_intent_id
            order = order_form.save()
            for colour_id, item_data in basket.items():
                try:
                    colour = get_object_or_404(Colour, pk=colour_id)
                    product = get_object_or_404(Product, pk=colour.product.id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        colour=colour,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist or Colour.DoesNotExist:
                    messages.error(request, (
                        'There was an error processing your basket. '
                        'Please call for further assistance.'),
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))

        else:
            messages.error(
                request,
                'Your form contains some invalid details. '
                'Please double check your information',
            )
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(
                request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        grand_total = current_basket['grand_total']
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=['card'],
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                saved_info = {
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                    'address_1': profile.default_address_1,
                    'address_2': profile.default_address_2,
                    'county': profile.default_county,
                }
                order_form = OrderForm(initial=saved_info)
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    context = {
        'checkout': True,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    This view displays details of a users order.
    The view also updates the user profile if the
    save-info box has been ticked.
    The session basket is also cleared.
    The "checkout success" boolean is used to
    identify the order progress.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
        if save_info:
            delivery_data = {
                'default_phone_number': order.phone_number,
                'default_address_1': order.address_1,
                'default_address_2': order.address_2,
                'default_city': order.city,
                'default_county': order.county,
                'default_country': order.country,
                'default_postcode': order.postcode,
            }
            user_data = {
                'first_name': order.full_name.split()[0],
                'last_name': order.full_name.split()[-1],
                'email': order.email,
            }
            user_profile_form = UserProfileForm(
                                    delivery_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

            user_form = UserForm(user_data, instance=request.user)
            if user_form.is_valid():
                user_form.save()

    if 'basket' in request.session:
        del request.session['basket']

    context = {
        'order': order,
        'checkout_success': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
