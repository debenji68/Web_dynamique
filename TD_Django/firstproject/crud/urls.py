from . import views
from django.urls import path
urlpatterns = [
    path('ajout', views.ajout),
    path('traitement', views.traitement), # ajouter la route traitement associé à l'action traitement du fichier views.py
    ]