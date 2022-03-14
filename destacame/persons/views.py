from django.shortcuts import render
from django.views.generic import ListView

from .models import Passenger, Driver


class ListPassengers(ListView):
    model = Passenger
    context_object_name = 'passengers'
    template_name = 'pages/passengers/list.html'


def create_passenger(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')

        if name:
            new_user = Passenger(name=name)
            new_user.save()

    return render(request, 'pages/passengers/create.html')


class ListDrivers(ListView):
    model = Driver
    context_object_name = 'drivers'
    template_name = 'pages/drivers/list.html'
