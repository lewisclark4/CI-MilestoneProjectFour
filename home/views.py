from django.shortcuts import render


def index(request):

    """ index page view """
    return render(request, "home/index.html")
