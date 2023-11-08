from django import forms


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', max_length=100, required=True)
    billing_address = forms.CharField(label='Billing Address', max_length=100, required=True)
    card_number = forms.CharField(label='Card Number', max_length=16, required=True)
    card_expiry = forms.CharField(label='Card Expiry (MM/YY)', max_length=5, required=True)
    card_cvc = forms.CharField(label='Card CVC', max_length=3, required=True)
