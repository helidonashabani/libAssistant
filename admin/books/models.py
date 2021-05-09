from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200,default="")
    author = models.CharField(max_length=200, default="")
    publisher = models.CharField(max_length=300, default="")
    status = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
