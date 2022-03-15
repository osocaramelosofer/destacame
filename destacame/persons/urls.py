from django.urls import path

from .views import (
    ListPassengers, ListDrivers,
    create_passenger, PassengerCreateView,
    PassengerDetail, PassengerEdit,

)

app_name = "persons"
urlpatterns = [
    path("list-drivers/", ListDrivers.as_view(), name='list-drivers'),
    path("list-passengers/", ListPassengers.as_view(), name='list-passengers'),

    path("create-passenger/", create_passenger, name='create-passenger'),
    path("new/", PassengerCreateView.as_view(), name='passenger_new'),

    path("person-detail/<int:pk>", PassengerDetail.as_view(), name="passenger_detail"),

    path("edit-passenger/<int:pk>", PassengerEdit.as_view(), name="passenger_edit"),

    # path("delete-passenger/<int:pk>", PassengerDelete.as_view(), name="passenger_delete"),
]
