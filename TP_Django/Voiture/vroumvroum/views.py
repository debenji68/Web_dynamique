from django.shortcuts import render
from .forms import ModeleForm,MarqueForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from . import models

def ajout(request):
    form = ModeleForm()  # création d'un formulaire vide
    return render(request, "vroumvroum/modele/ajout.html", {"form": form})

def traitementmodele(request):
    lform = ModeleForm(request.POST)
    if lform.is_valid():
        Modele = lform.save()
        return render(request, "vroumvroum/modele/affichemodele.html", {"Modele": Modele})
    else:
        return render(request, "vroumvroum/modele/ajout.html", {"form": lform})

def readmodele(request, id):
    Modele = models.Modele.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée
    return render(request, "vroumvroum/modele/affichemodele.html", {"Modele": Modele})

def allmodele(request):
    Modele = list(models.Modele.objects.all())
    return render(request, "vroumvroum/modele/all.html", {"Modele": Modele})

def traitementupdatemodele(request, id):
    modele = get_object_or_404(models.Modele, pk=id)

    if request.method == "POST":
        lform = ModeleForm(request.POST, instance=modele)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/vroumvroum/modele/")
        else:
            return render(request, "vroumvroum/modele/updatemodele.html", {"form": lform, "id": id})
    else:
        lform = ModeleForm(instance=modele)
        return render(request, "vroumvroum/modele/updatemodele.html", {"form": lform, "id": id})

def deletemodele(request, id):
    modele = get_object_or_404(models.Modele, pk=id)
    modele.delete()
    return HttpResponseRedirect("/vroumvroum/modele/")

def index(request):
    return render(request, 'vroumvroum/index.html')







def ajoutmarque(request):
    form = MarqueForm()  # création d'un formulaire vide
    return render(request, "vroumvroum/marque/ajoutmarque.html", {"form": form})

def traitement(request):
    lform = MarqueForm(request.POST)
    if lform.is_valid():
        Marque = lform.save()
        return render(request, "vroumvroum/marque/affichemarque.html", {"Marque": Marque})
    else:
        return render(request, "vroumvroum/marque/ajoutmarque.html", {"form": lform})

def read(request, id):
    Marque = models.Marque.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée
    return render(request, "vroumvroum/marque/affichemarque.html", {"Marque": Marque})

def all(request):
    Marque = list(models.Marque.objects.all())
    return render(request, "vroumvroum/marque/all.html", {"Marque": Marque})

def traitementupdate(request, id):
    marque = get_object_or_404(models.Marque, pk=id)

    if request.method == "POST":
        lform = MarqueForm(request.POST, instance=marque)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/vroumvroum/marque/")
        else:
            return render(request, "vroumvroum/marque/updatemarque.html", {"form": lform, "id": id})
    else:
        lform = MarqueForm(instance=marque)
        return render(request, "vroumvroum/marque/updatemarque.html", {"form": lform, "id": id})

def delete(request, id):
    marque = get_object_or_404(models.Marque, pk=id)
    marque.delete()
    return HttpResponseRedirect("/vroumvroum/marque/")