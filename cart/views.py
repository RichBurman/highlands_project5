from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from packages.models import Package


def add_to_cart(request, package_id):
    package = Package.objects.get(pk=package_id)
    user = request.user

    existing_cart_item, created = Cart.objects.get_or_create(
        user=user, package=package)

    if not created:
        existing_cart_item.quantity += 1
        existing_cart_item.save()

    return redirect('cart:cart_view')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()

    return redirect('cart:cart_view')


def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    total_price = sum(item.package.price *
                      item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
