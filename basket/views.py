from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ renders a view to see the products in the shopping basket """
    return render(request, "basket/basket.html")