from django.shortcuts import HttpResponse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product, Colour
from profiles.models import UserProfile
import json
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        This WH handler will check if an order has
        been created by the checkout view.
        If not, the handler will create the order
        and applicable order line items.
        This handler will also update the user
        profile if the payment intent meta data
        identifies that the save-info button
        was selected.
        """

        intent = event.data.object
        payment_intent_id = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for key, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[key] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    address_1__iexact=shipping_details.address.line1,
                    address_2__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    grand_total=grand_total,
                    stripe_payment_intent_id=payment_intent_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]}\
                    | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            profile = None
            username = intent.metadata.username
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_address_1 = shipping_details.address.line1
                    profile.default_address_2 = shipping_details.address.line2
                    profile.default_city = shipping_details.address.city
                    profile.default_county = shipping_details.address.state
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.save()
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    address_1=shipping_details.address.line1,
                    address_2=shipping_details.address.line2,
                    city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    stripe_payment_intent_id=payment_intent_id,
                )

                for colour_id, item_data in json.loads(basket).items():
                    colour = get_object_or_404(Colour, pk=colour_id)
                    product = get_object_or_404(Product, pk=colour.product.id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        colour=colour,
                        quantity=item_data,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}\
                | SUCCESS: Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
