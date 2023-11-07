from django.db import models

# Create your models here.


class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/packages/')
    average_review_rating = models.DecimalField(max_digits=3, decimal_places=2)
