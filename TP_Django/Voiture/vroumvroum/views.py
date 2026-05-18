from django.shortcuts import render
from .forms import ModeleForm,MarqueForm
from . import models

def ajout(request):
    if request.method == "POST":  # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = ModeleForm(request)
        if form.is_valid():  # validation du formulaire.
            Modele = form.save()  # sauvegarde dans la base
            return render(request, "vroumvroum/affiche.html", {"Modele": Modele})  #envoie vers une page d'affichage du Livre créé
        else:
            return render(request, "vroumvroum/ajout.html", {"form": form})
    else:
        form = ModeleForm()  # création d'un formulaire vide
        return render(request, "vroumvroum/ajout.html", {"form": form})