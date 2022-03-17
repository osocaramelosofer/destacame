from django.urls import path

from .views import ListRoutes, CreateRoute, DetailRoute, EditRoute, DeleteRoute


app_name = "routes"

urlpatterns = [
    path("list/", ListRoutes.as_view(), name="list_routes"),
    path("create/", CreateRoute.as_view(), name="create_route"),
    path("detail/<int:pk>", DetailRoute.as_view(), name="detail_route"),
    path("edit/<int:pk>", EditRoute.as_view(), name="edit_route"),
    path("delete/<int:pk>", DeleteRoute.as_view(), name="delete_route")
]
