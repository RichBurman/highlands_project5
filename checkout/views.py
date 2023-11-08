from django.shortcuts import render, redirect
from .models import Order, OrderItem, Payment
from .forms import CheckoutForm

def create_order(request):
    
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
            
            return redirect('checkout:order_confirmation', order.id)
    else:
        form = CheckoutForm()
    
    return render(request, 'checkout/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price})

def order_confirmation(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'checkout/order_confirmation.html', {'order': order})
