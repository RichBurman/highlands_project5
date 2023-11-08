from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.create_order, name='create_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.checkout_success, name='checkout_success'),
]
