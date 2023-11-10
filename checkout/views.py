from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, Payment
from .forms import CheckoutForm
from cart.models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request):
    cart = Cart.objects.filter(user=request.user)

    if not cart.exists():
        return redirect('cart:cart_view')

    total_price = sum(item.package.price * item.quantity for item in cart)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                addressline_1=form.cleaned_data['addressline_1'],
                addressline_2=form.cleaned_data['addressline_2'],
                county=form.cleaned_data['county'],
                country=form.cleaned_data['country'],
                phone_number=form.cleaned_data['phone_number'],
            )

            for cart_item in cart:
                OrderItem.objects.create(
                    order=order, package=cart_item.package, quantity=cart_item.quantity
                )

            Payment.objects.create(order=order, amount=total_price)

            cart.delete()

            return redirect('checkout:order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order': order})

def checkout_success(request, order_id):
    
    order = Order.objects.get(pk=order_id)

    return render(request, 'checkout/checkout_success.html', {'order': order})

def checkout(request):
    cart = Cart.objects.filter(user=request.user)

    if not cart.exists():
        return redirect('cart:cart_view')

    total_price = sum(item.package.price * item.quantity for item in cart)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(user=request.user, total_price=total_price)

            for cart_item in cart:
                OrderItem.objects.create(order=order, package=cart_item.package, quantity=cart_item.quantity)

            Payment.objects.create(order=order, amount=total_price)

            cart.delete()

            return redirect('checkout:order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price})

def process_checkout(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.package.price * item.quantity for item in cart)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            print("Form is valid. Creating order...")

            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                addressline_1=form.cleaned_data['addressline_1'],
                addressline_2=form.cleaned_data['addressline_2'],
                county=form.cleaned_data['county'],
                country=form.cleaned_data['country'],
                phone_number=form.cleaned_data['phone_number'],
            )

            for cart_item in cart:
                OrderItem.objects.create(
                    order=order, package=cart_item.package, quantity=cart_item.quantity
                )

            Payment.objects.create(order=order, amount=total_price)

            cart.delete()

            messages.success(request, 'Order placed successfully!')
            return redirect('checkout:checkout_success', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price})
