from django.urls import path
from . import views
from .views import update_cart

app_name = 'cart'

urlpatterns = [
    path('add/<int:package_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view/', views.view_cart, name='cart_view'),
    path('update/<int:item_id>/', update_cart, name='update_cart'),

]