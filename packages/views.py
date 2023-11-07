from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Package

# Create your views here.


class PackageListView(ListView):
    model = Package
    template_name = 'packages/package_list.html'
    context_object_name = 'packages'


class PackageDetailView(DetailView):
    model = Package
    template_name = 'packages/package_detail.html'
    context_object_name = 'package'


def package_list(request):
    packages = Package.objects.all()
    return render(request, 'packages/package_list.html', {'packages': packages})


def package_detail(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    return render(request, 'packages/package_detail.html', {'package': package})