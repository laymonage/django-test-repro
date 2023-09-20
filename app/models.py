from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        index_together = ["name", "author"]
