from django.db import models


class Women(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
