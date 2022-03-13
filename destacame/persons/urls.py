from django.urls import path

from .views import ListPassengers, ListDrivers

app_name = "persons"
urlpatterns = [
    path("list-drivers/", ListDrivers.as_view(), name='list-drivers'),
    path("list-passengers", ListPassengers.as_view(), name='list-passengers'),
]
