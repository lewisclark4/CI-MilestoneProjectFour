from django.shortcuts import HttpResponse, get_object_or_404
from .models import Order, OrderLineItem
from products.models import Product, Colour
import json
import time

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        payment_intent_id = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for key, value in shipping_details.address.items():
            if value == "":
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
            return HttpResponse(
                content=f'Webhook received: {event["type"]}\
                    | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
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
                    product  = get_object_or_404(Product, pk=colour.product.id)
                    order_line_item = OrderLineItem(
                        order=order, product=product, colour=colour, quantity=item_data,
                    )
                    order_line_item.save()                
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        return HttpResponse(
            content=f'Webhook received: {event["type"]}\
                | SUCCESS: Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)