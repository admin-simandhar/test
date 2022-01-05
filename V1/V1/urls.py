
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("auth/", include("AuthManager.urls")),
    path("head/", include("HeaderApp.urls")),
    path("leads/", include("Lead.urls")),
    path("student/", include("Students.urls")),
]
