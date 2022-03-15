from django.urls import path

from .views import ListBuses, CreateBuss, DetailBuss, EditBuss, DeleteBuss


app_name = "buses"
urlpatterns = [
    path("list/", view=ListBuses.as_view(), name="list"),
    path("craete/", view=CreateBuss.as_view(), name="create_buss"),
    path("detail/<int:pk>", view=DetailBuss.as_view(), name="buss_detail"),
    path("edit/<int:pk>", view=EditBuss.as_view(), name="edit_buss"),
    path("delete/<int:pk>", view=DeleteBuss.as_view(), name="delete_buss")

]
