from .views import ListBuses
from django.urls import path

app_name = "buses"
urlpatterns = [
    path("list/", view=ListBuses.as_view(), name="list"),
]
