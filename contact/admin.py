from django.contrib import admin
from .models import Subscription, SecureMessage

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)

admin.site.register(Subscription, SubscriptionAdmin)


class SecureMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'message', 'date_contacted')
    readonly_fields = ('name', 'email', 'message', 'date_contacted')
    ordering = ('-date_contacted',)
    
admin.site.register(SecureMessage, SecureMessageAdmin)

