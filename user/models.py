from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Custom User Model - User details


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    addressline_1 = models.CharField(max_length=50, blank=True)
    addressline_2 = models.CharField(max_length=50, blank=True)
    default_county = models.CharField(max_length=30, blank=True)
    default_country = CountryField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    discount_code = models.CharField(
        max_length=10, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

# UserProfile Model for Bio, Profile and will be used on reviews.


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
