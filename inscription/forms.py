from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = [
            'nom', 'prenom', 'niveau_etude', 'etablissement_origine', 
            'concours_souhaite', 'extrait_naissance', 'certificat', 
            'lettre_motivation', 'diplome', 'photo'
        ]
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_etude': forms.TextInput(attrs={'class': 'form-control'}),
            'etablissement_origine': forms.TextInput(attrs={'class': 'form-control'}),
            'concours_souhaite': forms.Select(attrs={'class': 'form-control'}),
            'extrait_naissance': forms.FileInput(attrs={'class': 'form-control'}),
            'certificat': forms.FileInput(attrs={'class': 'form-control'}),
            'lettre_motivation': forms.FileInput(attrs={'class': 'form-control'}),
            'diplome': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'niveau_etude': 'Niveau d\'études actuel',
            'etablissement_origine': 'Établissement d\'origine',
            'concours_souhaite': 'Concours souhaité',
            'extrait_naissance': 'Extrait de naissance (PDF)',
            'certificat': 'Certificat de scolarité (PDF)',
            'lettre_motivation': 'Lettre de motivation (PDF)',
            'diplome': 'Diplôme (PDF)',
            'photo': 'Photo d\'identité (JPG/PNG)',
        }