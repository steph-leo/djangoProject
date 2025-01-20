from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name = "main" ),
    path('workapp/', views.workapp, name = 'workapp'),
    path("workapp/details/<int:id>", views.details, name = "details"),
]