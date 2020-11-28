from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home.html"),
]