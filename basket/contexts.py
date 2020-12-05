from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

""" 
Context processor for the basket to allow basket
to be available across all apps.
"""

def basket_contents(request):


    empty_basket = True
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})

    for product_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += item_data * product.price
            product_count += item_data
            empty_basket = False
            basket_items.append(
                {"product_id": product_id, 
                "quantity": item_data, 
                "product": product,}
            )
        else:
            product = get_object_or_404(Product, pk=product_id)
            for quantity in item_data.items():
                total += quantity * product.price
                product_count += quantity
                empty_basket = False
                basket_items.append(
                    {
                        "product_id": product_id,
                        "quantity": quantity,
                        "product": product,
                    }
                )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "empty_basket": empty_basket,
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
