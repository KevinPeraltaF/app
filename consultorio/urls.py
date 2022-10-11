from django.urls import path, include
from django.contrib import admin

from consultorio.views import Dashboard

urlpatterns = [
    path('',Dashboard.as_view(), name= "dashboard"),
]


