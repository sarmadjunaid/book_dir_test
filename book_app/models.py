from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.genre


class Book(models.Model):
    name = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    synopsis = models.TextField(max_length=1000)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateTimeField()
    price = models.FloatField(verbose_name='Price in cents (¢)')
    
    
    def __str__(self):
        return self.name

    