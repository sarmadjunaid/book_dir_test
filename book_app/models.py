from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    synopsis = models.TextField(max_length=1000)
    genre = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    price = models.FloatField(verbose_name='Price in cents (¢)')
    
    
    def __str__(self):
        return self.name
