# admin.py
from django.contrib import admin
from .models import Order, OrderItem, Payment

class OrderAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ['user', 'total_price', 'address']

    def address(self, obj):
        return f'{obj.addressline_1}, {obj.addressline_2}, {obj.county}, {obj.country}, {obj.phone_number}'
    
    address.short_description = 'Address'

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
