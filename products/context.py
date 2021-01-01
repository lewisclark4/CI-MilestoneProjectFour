from .models import Category, Product


def all_categories(request):
    all_categories = Category.objects.all()

    context = {
        'all_categories': all_categories,
    }

    return context


def featured_products(request):
    featured_products = Product.objects.all().filter(featured=True)

    context = {
        'featured_products': featured_products,
    }

    return context
