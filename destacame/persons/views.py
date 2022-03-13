from django.shortcuts import render
from django.views.generic import ListView

from .models import Passenger, Driver


class ListPassengers(ListView):
    model = Passenger
    context_object_name = 'passengers'
    template_name = 'pages/passengers/list.html'


class ListDrivers(ListView):
    model = Driver
    context_object_name = 'drivers'
    template_name = 'pages/drivers/list.html'
