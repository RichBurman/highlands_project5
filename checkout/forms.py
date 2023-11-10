from django import forms
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    addressline_1 = forms.CharField()
    addressline_2 = forms.CharField(required=False)
    county = forms.CharField()
    country = CountryField().formfield()
    phone_number = forms.CharField()

    card_number = forms.CharField()
    card_expiry = forms.CharField()
    card_cvc = forms.CharField()
    terms_and_conditions = forms.BooleanField()