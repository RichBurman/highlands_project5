from django import forms
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    addressline_1 = forms.CharField()
    addressline_2 = forms.CharField(required=False)
    county = forms.CharField()
    country = CountryField().formfield()
    phone_number = forms.CharField()

    discount_code = forms.CharField(required=False)