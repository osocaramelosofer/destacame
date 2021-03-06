import datetime
from django.urls import reverse
from django.db import models

from ..buses.models import Buss
from ..routes.models import Route
from ..persons.models import Passenger, Driver


class Journey(models.Model):
    buss = models.ForeignKey('buses.Buss', on_delete=models.CASCADE)
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE)
    passenger = models.ForeignKey('persons.Passenger', on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey('persons.Driver', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return f'{self.route.destination}'

    def get_absolute_url(self):
        return reverse('journeys:journey_detail', args=[str(self.id)])
