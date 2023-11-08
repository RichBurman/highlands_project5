from django.urls import path
from allauth.account.views import SignupView, LoginView, LogoutView
from .views import user_profile, user_profile_edit, custom_user_edit, DisplayUserProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='user_signup'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/edit/', user_profile_edit, name='user_profile_edit'),
    path('user/edit/', custom_user_edit, name='custom_user_edit'),
    path('display_user_profile/<int:pk>/', DisplayUserProfileView.as_view(), name='display_user_profile'),
]
