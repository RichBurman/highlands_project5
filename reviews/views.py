from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Review
from .forms import ReviewForm
from django.views.generic import ListView
from packages.models import Package

# Create your views here.

class ReviewsListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

def review_list(request):
    packages = Package.objects.all()
    package_reviews = {}

    for package in packages:
        reviews = Review.objects.filter(package=package)
        package_reviews[package] = reviews

    return render(request, 'reviews/review_list.html', {'package_reviews': package_reviews, 'packages': packages})

def add_review(request, package_id):
    package = get_object_or_404(Package, pk=package_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.package = package 
            review.save()
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'package': package})

def view_review(request):
    packages = Package.objects.all()
    package_reviews = {}

    for package in packages:
        reviews = Review.objects.filter(package=package)
        package_reviews[package] = reviews

    return render(request, 'reviews/review_view.html', {'package_reviews': package_reviews})

def view_package_reviews(request, package_id):
    package = Package.objects.get(pk=package_id)
    reviews = Review.objects.filter(package=package)
    return render(request, 'reviews/package_reviews.html', {'package': package, 'reviews': reviews})

@method_decorator(login_required, name='dispatch')
class UserReviewsView(View):
    template_name = 'reviews/user_reviews.html'

    def get(self, request):
        user_reviews = Review.objects.filter(user=request.user)
        return render(request, self.template_name, {'user_reviews': user_reviews})

@method_decorator(login_required, name='dispatch')
class ReviewUpdateView(View):
    template_name = 'reviews/update_review.html'

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id, user=request.user)
        form = ReviewForm(instance=review)
        return render(request, self.template_name, {'form': form, 'review': review})

    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id, user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:user_reviews')
        return render(request, self.template_name, {'form': form, 'review': review})

@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(View):
    template_name = 'reviews/delete_review.html'

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id, user=request.user)
        return render(request, self.template_name, {'review': review})

    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id, user=request.user)
        review.delete()
        return redirect('reviews:user_reviews') 
