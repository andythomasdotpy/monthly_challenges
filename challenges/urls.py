from django.urls import path

from . import views

urlpatterns = [
    path("january", views.january , name="january"),
    path("february", views.february, name="february"),
    path("march", views.march, name="march"),
    path("<month>", views.monthly_challenge, name="monthly_challenge"),
]