from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Colour
from .forms import ProductForm, ColourForm

# Create your views here.

def all_products(request, category_slug=None):

    """
    To display all products, or products filter & sort dependent.
    """
    products = Product.objects.all()
    category= None
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

def product_detail(request, product_slug, category_slug):

    """ 
    returns the product detail view with all of the products information
    """
    category = Category.objects.get(slug=category_slug)
    product = Product.objects.get(
        category__slug=category_slug,
        slug=product_slug,
    )
    colours = Colour.objects.filter(product=product)

    context = {
        "product": product,
        "category": category,
        "colours": colours,
    }

    return render(request, "products/product_detail.html", context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added product')
            return redirect(reverse('add_colour'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    context = {
        'form': form,
    }

    return render(request, "products/add_product.html", context)

@login_required
def add_colour(request):
    if request.method == 'POST':
        form = ColourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added product colour')
            return redirect(reverse('add_colour'))
        else:
            messages.error(request, 'Failed to add product colour. Please ensure the form is valid.')
    else:
        form = ColourForm()
        
    context = {
        'form': form,
    }

    return render(request, "products/add_colour.html", context)