from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Colour

# Create your views here.

def view_basket(request):
    """ renders a view to see the products in the shopping basket """
    return render(request, "basket/basket.html")


def add_to_basket(request, product_id, colour_id=None):
    """Add products to the basket"""

    product = get_object_or_404(Product, pk=product_id)
    colour_id = request.POST.get('colour')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if colour_id in list(basket.keys()):
        basket[colour_id] += quantity
    else:
        basket[colour_id] = quantity

    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)