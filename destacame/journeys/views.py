from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy

from .models import Journey


class ListJourneys(ListView):
    model = Journey
    template_name = 'pages/journeys.html'
    context_object_name = 'journeys'


class JourneyDetail(DetailView):
    model = Journey
    template_name = 'pages/journeys/detail.html'


# class UpdateJourney(UpdateView):
#     model = Journey
#     template_name = ''
#     form_class = JourneyForm
#     success_url = reverse_lazy('')
