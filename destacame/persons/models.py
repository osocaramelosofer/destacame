from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)


class Driver(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
