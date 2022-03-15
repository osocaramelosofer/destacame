from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from .models import Passenger, Driver


class ListPassengers(ListView):
    model = Passenger
    context_object_name = 'passengers'
    template_name = 'pages/passengers/list.html'


class ListDrivers(ListView):
    model = Driver
    context_object_name = 'drivers'
    template_name = 'pages/drivers/list.html'


class PassengerCreateView(CreateView):
    model = Passenger
    template_name = 'pages/passengers/create.html'
    fields = ['name']


def create_passenger(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')

        if name:
            new_user = Passenger(name=name)
            new_user.save()

    return render(request, 'pages/passengers/create.html')


class PassengerDetail(DetailView):
    model = Passenger
    template_name = 'pages/passengers/detail.html'


class PassengerEdit(UpdateView):
    model = Passenger
    template_name = 'pages/passengers/edit_passenger.html'
    fields = ['name']


# class PassengerDelete(DeleteView):
#     model = Passenger
#     template_name = 'pages/passengers/delete.html'
#     success_url = 'persons:list-passengers'
