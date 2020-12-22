from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products, name="products"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/<int:product_id>/", views.edit_product, name="edit_product"),
    path("add_colour/", views.add_colour, name="add_colour"),
    path("<slug:category_slug>/", views.all_products, name="products_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
] 