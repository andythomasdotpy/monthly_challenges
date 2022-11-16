from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("challenges/", include("challenges.urls")),
    path("admin/", admin.site.urls),
]
