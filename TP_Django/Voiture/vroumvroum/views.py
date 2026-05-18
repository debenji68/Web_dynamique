from django.shortcuts import render
from .forms import ModeleForm,MarqueForm
from . import models

def ajout(request):
    form = ModeleForm()  # création d'un formulaire vide
    return render(request, "vroumvroum/ajout.html", {"form": form})

def ajoutmarque(request):
    form = MarqueForm()  # création d'un formulaire vide
    return render(request, "vroumvroum/ajoutmarque.html", {"form": form})

def traitement(request):
    lform = MarqueForm(request.POST)
    if lform.is_valid():
        Marque = lform.save()
        return render(request, "vroumvroum/affichemarque.html", {"Marque": Marque})
    else:
        return render(request, "vroumvroum/ajoutmarque.html", {"form": lform})

def read(request, id):
    Marque = models.Marque.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée
    return render(request, "vroumvroum/affiche.html", {"Marque": Marque})