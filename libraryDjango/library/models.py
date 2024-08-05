from django.db import models


class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    readCheck = models.BooleanField
    slug = models.SlugField()

    def __str__(self):
        return self.title