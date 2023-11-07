from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Package._meta.get_fields()]
    list_filter = ('title', 'price')
    search_fields = ('title', 'description')
