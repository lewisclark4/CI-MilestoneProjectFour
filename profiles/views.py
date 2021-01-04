from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, UserForm


@login_required
def profile(request):

    form = UserForm(instance=request.user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your details were updated successfully')
        else:
            messages.warning(
                request, ('There was an error updating your details.'
                          + ' Please try again.'))
    context = {
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def delivery_details(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your delivery details were updated successfully')
        else:
            messages.warning(
                request, ('There was an error updating your details.'
                          + ' Please try again.'))

    context = {
        'form': form,
    }

    return render(request, 'profiles/delivery.html', context)


@login_required
def order_history(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-date_ordered')

    context = {
         'orders': orders,
    }

    return render(request, 'profiles/order_history.html', context)
