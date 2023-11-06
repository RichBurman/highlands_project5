from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery, name='gallery'),
]
