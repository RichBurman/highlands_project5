from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem, Payment, DiscountCode
from .forms import CheckoutForm
from cart.models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from decimal import Decimal
import stripe
from django.conf import settings


def create_order(request):
    cart = Cart.objects.filter(user=request.user)

    if not cart.exists():
        return redirect('cart:cart_view')

    total_price = sum(item.package.price * item.quantity for item in cart)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            discount_code = form.cleaned_data.get('discount_code', '')
            discount_amount = calculate_discount(total_price, discount_code)

            order = Order.objects.create(
                user=request.user,
                total_price=total_price - discount_amount,
                discount_amount=discount_amount,
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

            Payment.objects.create(order=order, amount=total_price - discount_amount)

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

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_checkout(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.package.price * item.quantity for item in cart)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    form = CheckoutForm()

    discount_amount = 0


    # Create a PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=int((total_price - discount_amount) * 100),
        currency='gbp',
        description='Order payment',
    )

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            

            discount_code = form.cleaned_data.get('discount_code', '')
            discount_amount = calculate_discount(total_price, discount_code)

            total_amount = total_price - discount_amount

            
            order = Order.objects.create(
                user=request.user,
                total_price=total_price - discount_amount,
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

            Payment.objects.create(order=order, amount=total_price - discount_amount)

            cart.delete()

            messages.success(request, 'Order placed successfully! Your Adventure Begins!')
            client_secret = intent.client_secret
            return render(request, 'checkout/checkout_success.html', {'order': order, 'client_secret': client_secret, 'public_key': stripe_public_key})
        else:
            messages.error(request, 'Error processing your order. Please try again.')
            return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price, 'client_secret': client_secret, 'public_key': stripe_public_key})
            
            
    
    client_secret = intent.client_secret
    return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price, 'client_secret': client_secret, 'public_key': stripe_public_key})





def calculate_discount(total_price, discount_code):
    if not discount_code:
        return 0  # No discount code provided

    try:
        code = DiscountCode.objects.get(code=discount_code)
        return total_price * (code.discount_percentage / 100)
    except DiscountCode.DoesNotExist:
        return 0  # Invalid discount code



def validate_discount(request, discount_code):
    try:
        code = DiscountCode.objects.get(code=discount_code)
        return JsonResponse({'valid': True, 'discount_percentage': float(code.discount_percentage)})
    except DiscountCode.DoesNotExist:
        return JsonResponse({'valid': False})