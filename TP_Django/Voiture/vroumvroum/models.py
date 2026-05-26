from django.db import models

class Marque(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    fondateur = models.CharField(max_length = 100)
    date_creation = models.DateField(blank=True, null = True) # champs de type date,pouvant être null ou ne pas être rempli
    pays_origine = models.CharField(max_length = 50)
    resume = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
        chaine = f"{self.nom} fonder par {self.fondateur} le {self.date_creation} en {self.pays_origine}"
        return chaine

from django.db import models

class Modele(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    energie = models.CharField(max_length=100)
    nombre_chevaux = models.IntegerField(blank=False)
    type_moteur = models.CharField(max_length=100)
    prix = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True) # champs de type text long
    marque = models.ForeignKey("Marque", on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='modeles/', null=True, blank=False)
    def __str__(self):
        chaine = f"{self.nom}, {self.energie}, {self.nombre_chevaux}, {self.type_moteur}, {self.prix}, {self.marque}"
        return chaine