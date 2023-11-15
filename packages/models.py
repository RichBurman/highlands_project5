from django.db import models

# Create your models here.


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/packages/')
    
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Difficult', 'Difficult'),
        ('Challenging', 'Challenging'),
    )

    difficulty_rating = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='Easy'
    )
    
