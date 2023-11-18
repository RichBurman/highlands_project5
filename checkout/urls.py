from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('checkout/', views.process_checkout, name='checkout'),
    path('checkout/success/<int:order_id>/', views.checkout_success, name='checkout_success'),
    path('validate_discount/<str:discount_code>/', views.validate_discount, name='validate_discount'),
]