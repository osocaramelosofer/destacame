from django.urls import path

from .views import ListPassengers, ListDrivers, create_passenger

app_name = "persons"
urlpatterns = [
    path("list-drivers/", ListDrivers.as_view(), name='list-drivers'),
    path("list-passengers/", ListPassengers.as_view(), name='list-passengers'),
    path("create-passenger/", create_passenger, name='create-passenger')
]
