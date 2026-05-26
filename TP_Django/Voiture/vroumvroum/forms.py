from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class MarqueForm(ModelForm):
    class Meta:
        model = models.Marque
        fields = ('nom', 'fondateur', 'date_creation', 'pays_origine', 'resume')
        labels = {
            'nom': _('Nom'),
            'fondateur': _('Fondateur'),
            'date_creation': _('date de creation'),
            'pays_origine': _('pays origine'),
            'resume': _('Résumé')
        }


class ModeleForm(ModelForm):
    class Meta:
        model = models.Modele
        fields = ('nom', 'energie', 'nombre_chevaux', 'type_moteur', 'prix', 'resume', 'marque', 'image')
        labels = {
            'nom': _('Nom'),
            'energie': _('Energie'),
            'nombre_chevaux': _('nombre de chevaux'),
            'type_moteur': _('type de moteur'),
            'prix': _('Prix'),
            'resume': _('Résumé'),
            'marque': _('Marque'),
            'image': _('Image'),
        }