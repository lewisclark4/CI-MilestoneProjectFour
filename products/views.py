from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Colour

# Create your views here.

def all_products(request):

    """
    To display all products, or products filter dependent.
    """
    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if "category" in request.GET:
            category = request.GET["category"]
            products = products.filter(category__name__iexact=category)
            category = Category.objects.filter(
                    name__iexact=category)

        if "q" in request.GET:
            query = request.GET["q"]
            
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse("products"))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search" : query,
        "category_selection": category_selection,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):

    """ 
    returns the product detail view with all of the products information
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)