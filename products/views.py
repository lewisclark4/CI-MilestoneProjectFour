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
    sort = None
    direction= None

    if request.GET:

        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)
        else:
            products = Product.objects.all()

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
    
    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search" : query,
        "category": category,
        "current_sorting": current_sorting,
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