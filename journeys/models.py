from django.db import models

# Create your models here.
class Journey(models.Model):
    buss = models.IntegerField()
    route = models.IntegerField()
