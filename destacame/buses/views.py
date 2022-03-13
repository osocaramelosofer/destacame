from django.shortcuts import render
from django.views.generic import ListView

from .models import Buss

class ListBuses(ListView):
    model = Buss
    context_object_name = 'buses'
    template_name = 'pages/buses/list.html'
