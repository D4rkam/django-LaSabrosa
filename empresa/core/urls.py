from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("visit/", views.visit, name="visit"),
    path("history/", views.history, name="history"),
]