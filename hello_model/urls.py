from django.urls import path

from .views import user_create, user_delete, user_list, user_update

urlpatterns = [
    path("users/", user_list),
    path("users/<int:user_id>/create/", user_create),
    path("users/<int:user_id>/update/", user_update),
    path("users/<int:user_id>/delete/", user_delete),
]
