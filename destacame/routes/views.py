from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Route


class ListRoutes(ListView):
    model = Route
    template_name = 'pages/routes/list.html'
    context_object_name = 'routes'


class CreateRoute(CreateView):
    model = Route
    template_name = 'pages/routes/create.html'
    fields = ['origin', 'destination']


class DetailRoute(DetailView):
    model = Route
    template_name = 'pages/routes/detail.html'


class EditRoute(UpdateView):
    model = Route
    template_name = 'pages/routes/edit.html'
    fields = ['origin', 'destination']


class DeleteRoute(DeleteView):
    model = Route
    template_name = 'pages/routes/delete.html'
    success_url = reverse_lazy('routes:list_routes')
