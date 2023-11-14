# admin.py
from django.contrib import admin
from .models import Order, OrderItem, Payment, DiscountCode


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(DiscountCode)