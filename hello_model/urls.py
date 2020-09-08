from django.urls import path

from .views import user_list, user_create

urlpatterns = [
    path("users/", user_list),
    path("users/<int:user_id>", user_create),
]
