from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Journey

# Create your views here.
class ListJourneys(ListView):
    model = Journey
    template_name = 'pages/journeys.html'
    context_object_name = 'journeys'
