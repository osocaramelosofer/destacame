from django.utils.translation import gettext_lazy as _

from django.db import models
# from destacame.destacame.buses.models import Buss2
from ..buses.models import Buss
# from ..routes.models import Route
# from destacame.buses.models import Buss2
# from ..persons.models import Passenger, Driver

# Create your models here.
class Journey(models.Model):
    # buss = models.IntegerField()
    route = models.IntegerField()
    passenger = models.IntegerField()

    buss = models.ForeignKey('buses.Buss', on_delete=models.CASCADE)
    # route = models.ForeignKey('Route', on_delete=models.CASCADE)
    # passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    # driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    # date = models.DateField()

