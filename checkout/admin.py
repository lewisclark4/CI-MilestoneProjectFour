from django.contrib import admin
from .models import Order, OrderLineItem
from products.models import Product, Colour

class OrderLineItemAdminInline(admin.TabularInline):
    """ Allows adding and editing inline items from the order model"""
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date_ordered',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date_ordered', 'full_name',
              'email', 'phone_number', 'address1',
              'address2', 'city', 'county',
              'country', 'postcode', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date_ordered', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date_ordered',)


admin.site.register(Order, OrderAdmin)