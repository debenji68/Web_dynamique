from . import views
from django.urls import path
urlpatterns = [
    path("index/", views.index),
    path('ajout', views.ajout),
    ]