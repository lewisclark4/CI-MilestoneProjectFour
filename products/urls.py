from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products, name="products"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete_product/<int:product_id>/", views.delete_product, name="delete_product"),
    path("add_colour/", views.add_colour, name="add_colour"),
    path("edit_colour/<int:colour_id>/", views.edit_colour, name="edit_colour"),
    path("delete_colour/<int:colour_id>/", views.delete_colour, name="delete_colour"),
    path("<slug:category_slug>/", views.all_products, name="products_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
] 