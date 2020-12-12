from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Product, Colour

# Create your views here.

def view_basket(request):
    """ renders a view to see the products in the shopping basket """
    return render(request, "basket/basket.html")


def add_to_basket(request, product_id):
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
    return redirect(redirect_url)


def update_basket(request, colour_id):
    """updates products in the basket"""

    colour = get_object_or_404(Colour, pk=colour_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[colour_id] = quantity
    else:
        basket.pop(colour_id)

    request.session['basket'] = basket
    return redirect(reverse("view_basket"))

def remove_from_basket(request, colour_id):
    """Remove the product from the shopping basket"""

    colour = get_object_or_404(Colour, pk=colour_id)
    basket = request.session.get('basket', {})

    basket.pop(colour_id)

    request.session["basket"] = basket
    return redirect(reverse("view_basket"))
