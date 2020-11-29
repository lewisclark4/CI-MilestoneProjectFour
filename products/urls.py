from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products, name="products"),
    path("<slug:slug>/", views.all_products, name="products_by_category"),
    path('<product_id>', views.product_detail, name="product_detail"),
] 