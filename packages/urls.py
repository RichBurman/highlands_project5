from django.urls import path
from . import views  # Import the views module from the same app
from .views import PackageListView

app_name = 'packages'

urlpatterns = [
    path('packages/', PackageListView.as_view(), name='package_list'),
    path('packages/<int:package_id>/', views.package_detail,
         name='package_detail'),  # Use the views module for package_detail
]
