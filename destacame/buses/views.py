from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Buss


class ListBuses(ListView):
    model = Buss
    context_object_name = 'buses'
    template_name = 'pages/buses/list.html'


class CreateBuss(CreateView):
    model = Buss
    template_name = 'pages/buses/create.html'
    fields = ['plate', 'name']


class DetailBuss(DetailView):
    model = Buss
    template_name = 'pages/buses/detail.html'


class EditBuss(UpdateView):
    model = Buss
    template_name = 'pages/buses/edit.html'
    fields = ['plate', 'name']


class DeleteBuss(DeleteView):
    model = Buss
    template_name = 'pages/buses/delete.html'
    success_url = reverse_lazy('buses:list')
