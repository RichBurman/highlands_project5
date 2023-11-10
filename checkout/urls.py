from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('checkout/success/<int:order_id>/', views.checkout_success, name='checkout_success'),
]
