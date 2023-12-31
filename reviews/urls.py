from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.review_list, name='review_list'),
    path('add_review/<int:package_id>/', views.add_review, name='add_review'),
    path('reviews_list/', views.ReviewsListView.as_view(), name='reviews_list'),
    path('view_review/', views.view_review, name='view_review'),
    path('view_package_reviews/<int:package_id>/', views.view_package_reviews, name='view_package_reviews'),
    path('user-reviews/', views.UserReviewsView.as_view(), name='user_reviews'),
    path('review/<int:review_id>/update/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:review_id>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
]
