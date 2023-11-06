from django import forms
from .models import CustomUser, UserProfile


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'addressline_1', 'addressline_2',
                  'default_county', 'default_country', 'phone_number')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture')
