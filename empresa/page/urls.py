from django.urls import path
from . import views

urlpatterns = [
    path("other/<page_id>", views.other, name="other"),
]