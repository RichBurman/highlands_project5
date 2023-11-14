from django.db import models
from cart.models import Cart
from user.models import CustomUser
from packages.models import Package
from django_countries.fields import CountryField

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    addressline_1 = models.CharField(max_length=50, blank=True)
    addressline_2 = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=30, blank=True)
    country = CountryField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'Order for {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.package.title}'


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment for Order {self.order.id}'


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}% Discount"