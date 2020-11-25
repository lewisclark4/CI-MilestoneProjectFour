from django.shortcuts import render
from .models import Product, Category, Colour

# Create your views here.

def all_products(request):

    """
    To display all products, or products filter dependent.
    """
    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)
