from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
