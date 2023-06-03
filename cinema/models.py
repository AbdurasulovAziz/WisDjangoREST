from django.contrib.auth import get_user_model
from django.db import models

from cinema.model_validators import check_correct_datetime


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    age_limit = models.IntegerField(default=0)
    director = models.CharField(max_length=255)
    trailer = models.SlugField()

    def __str__(self):
        return self.name


class Seance(models.Model):
    film = models.ForeignKey(Film, related_name='seance', on_delete=models.CASCADE)
    datetime = models.DateTimeField(validators=[check_correct_datetime])
    price = models.IntegerField(default=0)
