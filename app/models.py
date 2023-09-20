from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        indexes = [models.Index(fields=["name", "author"])]
