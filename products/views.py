from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Colour

# Create your views here.

def all_products(request, category_slug=None):

    """
    To display all products, or products filter dependent.
    """
    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction= None


    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = Product.objects.filter(
                category=category.id).order_by(sortkey)
        else:
            products = Product.objects.filter(
                category=category.id)
    else:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = Product.objects.order_by(sortkey)
        else:
            products = Product.objects.all()
            

    context = {
        "products": products,
        "category": category,
    }

    return render(request, "products/products.html", context)
"""
   
        if "q" in request.GET:
            query = request.GET["q"]
            
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse("products"))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
"""
def product_detail(request, name):

    """ 
    returns the product detail view with all of the products information
    """

    product = get_object_or_404(Product, name)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)