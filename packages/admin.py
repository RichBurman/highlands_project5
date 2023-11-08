from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'average_review_rating']
    list_filter = ('title', 'price')
    search_fields = ('title', 'description')
