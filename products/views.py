from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Colour
from .forms import ProductForm, ColourForm


def all_products(request, category_slug=None):

    """
    This view is used to display products
    dependent on a users selection.
    This view also enables sorting products
    on price.
    """
    products = Product.objects.all()
    category = None
    direction = None

    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = Product.objects.filter(
                category=category.id).order_by(sortkey)
        else:
            products = Product.objects.filter(
                category=category.id)
    else:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = Product.objects.order_by(sortkey)
        else:
            products = Product.objects.all()

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'products/products.html', context)


def featured_products(request):
    """
    This view is used to display
    featured products.
    This view also enables sorting products
    on price.
    """

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = Product.objects.filter(
            featured=True).order_by(sortkey)
    else:
        products = Product.objects.filter(
            featured=True)

    context = {
        'featured': True,
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_slug, category_slug):
    """
    This view is used to return the product
    detail view with all of the products'
    information
    """
    category = Category.objects.get(slug=category_slug)
    product = Product.objects.get(
        category__slug=category_slug,
        slug=product_slug,
    )
    colours = Colour.objects.filter(product=product)
    count_colours = Colour.objects.filter(product=product).count()

    context = {
        'product': product,
        'category': category,
        'colours': colours,
        'count': count_colours,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    This view enables a superuser to add new products
    and will validate the form before submission.
    The view will prevent non authorised access.
    """

    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added product')
            return redirect(reverse('add_colour'))
        else:
            messages.error(
                request, 'Failed to add product. '
                         + 'Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """
    This view enables a superuser to update product information
    and will validate the form before submission.
    The view will prevent non authorised access.
    """

    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('product_detail',
                                args=[product.category.slug,
                                      product.slug],))

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.product_name} was updated')
            return redirect(reverse('product_detail',
                                    args=[product.category.slug,
                                          product.slug],))
        else:
            messages.error(request, f'Failed to update {product.product_name}.'
                                    + ' Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """
    This view enables an admin user to delete a product.
    The view will prevent non authorised access.
    """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('product_detail',
                                args=[product.category.slug,
                                      product.slug],))

    product.delete()
    messages.success(request, f'{product.product_name} was deleted.')
    return redirect(reverse('products'))


@login_required
def add_colour(request):
    """
    This view enables a superuser to add new products
    colours and will validate the form before submission.
    The view will prevent non authorised access.
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ColourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added product colour')
            return redirect(reverse('add_colour'))
        else:
            messages.error(
                request, 'Failed to add product colour. '
                         + 'Please ensure the form is valid.')
    else:
        form = ColourForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_colour.html', context)


@login_required
def edit_colour(request, colour_id):
    """
    This view enables a superuser user to update product colours
    and will validate the form before submission.
    The view will prevent non authorised access.
    """
    colour = get_object_or_404(Colour, pk=colour_id)
    product = get_object_or_404(Product, pk=colour.product.id)

    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('product_detail',
                                args=[product.category.slug,
                                      product.slug],))

    if request.method == 'POST':
        form = ColourForm(request.POST, instance=colour)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.product_name} - '
                                      + '{colour.colour} was updated')
            return redirect(reverse('product_detail',
                                    args=[product.category.slug,
                                          product.slug],))
        else:
            messages.error(request, f'Failed to update {product.product_name}'
                                    + ' - {colour.colour}. '
                                    + 'Please ensure the form is valid.')
    else:
        form = ColourForm(instance=colour)

    context = {
        'form': form,
        'product': product,
        'colour': colour,
    }

    return render(request, 'products/edit_colour.html', context)


@login_required
def delete_colour(request, colour_id):
    """
    This view enables an admin user to delete a product colour.
    The view will prevent non authorised access.
    """
    colour = get_object_or_404(Colour, pk=colour_id)
    product = get_object_or_404(Product, pk=colour.product.id)

    if not request.user.is_superuser:
        messages.error(
            request, 'You do not have the correct permissions '
                     + 'to complete this action.')
        return redirect(reverse('product_detail',
                                args=[product.category.slug,
                                      product.slug],))

    colour.delete()
    messages.success(request, f'{product.product_name}'
                              + ' - {colour.colour} was deleted.')
    return redirect(reverse('products'))
