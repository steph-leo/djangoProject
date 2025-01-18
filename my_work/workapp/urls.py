from django.urls import path
from . import views

urlpatterns = [
    path("", views.workapp, name = "workapp" ),
    path("details/<int:id>", views.details, name = "details"),
]