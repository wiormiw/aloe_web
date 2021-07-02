from django.db import models
from django.contrib import admin

# Create your models here.
class Command(models.Model):
    name = models.CharField(max_length=30)
    command = models.CharField(max_length=30, default="")
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.name    