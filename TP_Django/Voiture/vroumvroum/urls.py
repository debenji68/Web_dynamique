from . import views
from django.urls import path
urlpatterns = [
    path('modele/ajout/', views.ajout),
    path('modele/traitementmodele/', views.traitementmodele),
    path('modele/affichemodele/', views.readmodele),
    path('modele/', views.allmodele),
    path('modele/updatemodele/<int:id>/', views.traitementupdatemodele),
    path('modele/deletemodele/<int:id>/', views.deletemodele),
    path('marque/ajoutmarque/', views.ajoutmarque),
    path('marque/traitement/',views.traitement),
    path('marque/affichemarque/<int:id>/',views.read),
    path('marque/', views.all),
    path('marque/updatemarque/<int:id>/', views.traitementupdate),
    path('marque/deletemarque/<int:id>/', views.delete),
    path('index/', views.index),
    ]