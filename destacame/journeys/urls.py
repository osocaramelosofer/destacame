from django.urls import path

from .views import ListJourneys
app_name = "journeys"
urlpatterns = [
    path("list/", view=ListJourneys.as_view(), name="list"),
]
