from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
