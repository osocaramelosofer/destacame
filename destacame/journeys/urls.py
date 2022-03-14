from django.urls import path

from .views import ListJourneys, JourneyDetail

app_name = "journeys"
urlpatterns = [
    path("list/", view=ListJourneys.as_view(), name="list"),
    path("detail/<int:pk>", view=JourneyDetail.as_view(), name="journey_detail"),
]
