from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product
from django.db.models import Q


def search_result(request):
    """
    Product name, brand name, category & description
    are all queried for matches based on the search
    """
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.warning(request, 'Please enter a search criteria')
            return redirect(reverse('products'))
        products = Product.objects.all().filter(
            Q(product_name__icontains=query)
            | Q(description__icontains=query)
            | Q(brand_name__icontains=query)
            | Q(category__friendly_name__icontains=query)
        )

    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'search/search.html', context)
