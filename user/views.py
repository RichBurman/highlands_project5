from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser, UserProfile
from .forms import CustomUserForm, UserProfileForm

# View the User Profile
@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'user/user_profile.html', {'user_profile': user_profile})

# User Profile - Edit Bio and Profile Picture
@login_required
def user_profile_edit(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            return redirect('user_profile')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user/user_profile_edit.html', {'form': form, 'user_profile': user_profile})


# User Profile -  Edit CustomUser data
@login_required
def custom_user_edit(request):
    custom_user = CustomUser.objects.get(pk=request.user.pk)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=custom_user)

        if form.is_valid():
            form.save()
            return redirect('user_profile')

    else:
        form = CustomUserForm(instance=custom_user)

    return render(request, 'user/custom_user_edit.html', {'form': form, 'custom_user': custom_user})
