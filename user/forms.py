from django import forms
from django_countries.fields import CountryField
from .models import CustomUser, UserProfile

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'addressline_1', 'addressline_2', 'county', 'country', 'phone_number']


class UserProfileForm(forms.ModelForm):
    country = CountryField().formfield()

    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture', 'country')