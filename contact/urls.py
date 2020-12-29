from django.urls import path
from . import views


urlpatterns = [
    path("", views.secure_message, name="contact"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("faqs/", views.faqs, name="faqs"),
    path("about/", views.about, name="about"),
]