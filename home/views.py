from django.shortcuts import render


def index(request):

    """ index/ home page view """
    return render(request, 'home/index.html')
