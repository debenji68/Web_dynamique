from django.shortcuts import render
from .forms import ModeleForm,MarqueForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
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

def all(request):
    Marque = list(models.Marque.objects.all())
    return render(request, "vroumvroum/all.html", {"Marque": Marque})

def traitementupdate(request, id):
    marque = get_object_or_404(models.Marque, pk=id)

    if request.method == "POST":
        lform = MarqueForm(request.POST, instance=marque)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/vroumvroum/")
        else:
            return render(request, "vroumvroum/updatemarque.html", {"form": lform, "id": id})
    else:
        lform = MarqueForm(instance=marque)
        return render(request, "vroumvroum/updatemarque.html", {"form": lform, "id": id})

def delete(request, id):
    marque = get_object_or_404(models.Marque, pk=id)
    marque.delete()
    return HttpResponseRedirect("/vroumvroum/")