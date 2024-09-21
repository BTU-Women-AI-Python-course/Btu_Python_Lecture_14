from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
