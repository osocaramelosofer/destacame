from django.db import models

# Create your models here.
class Route(models.Model):
    origin = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
