from .models import Category

def all_categories(request):
    all_categories = Category.objects.all()
    
    context = {
        "all_categories": all_categories,
    }

    return context