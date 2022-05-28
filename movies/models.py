from django.core import validators
from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.FloatField(null=True, validators=[validators.MaxValueValidator(10.0)])
    description = models.TextField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    trailer = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title