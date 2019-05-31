from django.db import models

# Create your models here.

from django.db import models


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    preparation_time = models.PositiveIntegerField()
    preparation_guide = models.TextField()

    def __str__(self):
        return f'Recipe: {self.name}'