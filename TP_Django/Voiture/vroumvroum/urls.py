from . import views
from django.urls import path
urlpatterns = [
    path('ajout/', views.ajout),
    path('ajoutmarque/', views.ajoutmarque),
    path('traitement/',views.traitement),
    path('affiche/<int:id>/',views.read),
    ]