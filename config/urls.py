from django.urls import include, path

urlpatterns = [
    path("hello/", include("hello_model.urls")),
]
