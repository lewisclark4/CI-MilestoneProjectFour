from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your delivery details were updated successfully')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def order_history(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-date_ordered')

    context = {
         'orders': orders,
    }

    return render(request, 'profiles/order_history.html', context)
