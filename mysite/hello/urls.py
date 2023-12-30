from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.hello_view, name="index")
]
