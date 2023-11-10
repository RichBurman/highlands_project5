from django import forms
from .models import CustomUser, UserProfile


from django import forms
from django_countries.fields import CountryField

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'addressline_1', 'addressline_2', 'county', 'country', 'phone_number', 'discount_code']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture')
