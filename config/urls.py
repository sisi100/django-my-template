from django.urls import include, path

urlpatterns = [
    path("hello/", include("hello_world_app.urls")),
]
