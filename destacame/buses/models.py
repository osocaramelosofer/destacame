from django.db import models

# Create your models here.
class Buss(models.Model):
    plate = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
