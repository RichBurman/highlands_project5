from django.db import models
from django.conf import settings
from packages.models import Package


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult'),
        ('challenging', 'Challenging'),
    )

    difficulty_rating = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='easy'
    )

    OVERALL_RATING_CHOICES = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor'),
        ('very_poor', 'Very Poor'),
    )

    overall_rating = models.CharField(
        max_length=20,
        choices=OVERALL_RATING_CHOICES,
        default='good'
    )

    def __str__(self):
        return f"Review by {self.user} at {self.created_at} for {self.package}"
