from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.urls import reverse
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
