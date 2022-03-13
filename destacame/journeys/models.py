
from django.db import models
from ..buses.models import Buss
from ..routes.models import Route
from ..persons.models import Passenger, Driver

# Create your models here.
class Journey(models.Model):
    buss = models.ForeignKey('Buss', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    date = models.DateField()
