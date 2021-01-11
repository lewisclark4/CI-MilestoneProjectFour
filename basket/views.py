from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from products.models import Product, Colour


def view_basket(request):
    """ renders a view to see the products in the shopping basket """
    return render(request, "basket/basket.html")


def add_to_basket(request, product_id):
    """ This view enables adding products to the session.
        The basket is passed the colour ID of a product
        (as this is unique to a product).
        The basket it passed the quanitity from the
        input form on the product detail page.
        The user is redirected back to the product
        page, with a success message.
    """
    product = get_object_or_404(Product, pk=product_id)
    colour_id = request.POST.get('colour')
    colour = get_object_or_404(Colour, pk=colour_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if colour_id in list(basket.keys()):
        basket[colour_id] += quantity
        messages.success(
            request, (f'Successfully added {quantity} x '
                      + f'{product.product_name} '
                      + f'({colour.colour}) to your basket'))
    else:
        basket[colour_id] = quantity
        messages.success(
            request, (f'Successfully added {quantity} x '
                      + f'{product.product_name} '
                      + f'({colour.colour}) to your basket'))

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, colour_id):
    """ This view enables updating session basket items.
        Items are removed from the basket if the quantity is zero.
        The basket is updated with the appropriate
        quanitity if a numeric value other than 0
    """

    colour = get_object_or_404(Colour, pk=colour_id)
    product = get_object_or_404(Product, pk=colour.product.id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[colour_id] = quantity
        messages.success(
            request, (f'Successfully updated {product.product_name} '
                      + f'({colour.colour}) quantity to {quantity}'))
    else:
        basket.pop(colour_id)
        messages.success(
            request, (f'Successfully removed {product.product_name} '
                      + f'({colour.colour}) from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, colour_id):
    """This view enables removing session basket items."""

    colour = get_object_or_404(Colour, pk=colour_id)
    product = get_object_or_404(Product, pk=colour.product.id)
    basket = request.session.get('basket', {})

    basket.pop(colour_id)
    messages.success(
            request, (f'Successfully removed {product.product_name} '
                      + f'({colour.colour}) from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
