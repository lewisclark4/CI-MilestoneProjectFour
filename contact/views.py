from django.shortcuts import render, redirect
from .models import Subscription
from .forms import SubscriptionForm
from django.contrib import messages

# Create your views here.

def subscribe(request):
    
    sub_form = SubscriptionForm()
    subscribe_redirect = request.POST.get('subscribe_redirect')
    if request.method == "POST":
        sub_form = SubscriptionForm(request.POST)
        if Subscription.objects.filter(
            email=request.POST.get("email")
        ).exists():
            messages.info(
                request, "You are aleady subscribed to our newsletter."
            )
            return redirect(subscribe_redirect)
        else:
            if sub_form.is_valid():
                sub_form.save()
                messages.success(request, "You are now subscribed to our newsletter.")
    return redirect(subscribe_redirect)