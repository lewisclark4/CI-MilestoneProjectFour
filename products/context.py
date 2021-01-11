from .models import Category, Product


def all_categories(request):
    """
    This context processor allows all categories
    to be accessed across the site, for example
    the navbar links & home page links
    """
    all_categories = Category.objects.all()

    context = {
        'all_categories': all_categories,
    }

    return context


def featured_products(request):
    """
    This context processor allows all featured
    products to be accessed across the site for the
    featured products slider
    """
    featured_products = Product.objects.all().filter(featured=True)

    context = {
        'featured_products': featured_products,
    }

    return context
