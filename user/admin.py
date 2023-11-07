from django.contrib import admin
from .models import CustomUser, UserProfile

# Custom User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'email', 'phone_number', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'default_country')

# UserProfile 

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
    search_fields = ('user__username', 'bio')
    list_filter = ('user__is_staff', 'user__is_superuser')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
