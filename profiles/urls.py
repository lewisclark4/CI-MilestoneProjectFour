from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('delivery/', views.delivery_details, name='delivery'),
    path('order_history/', views.order_history, name='order_history'),
]
