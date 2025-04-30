from django.db import models

class Inscription(models.Model):
    NIVEAU_CHOICES = [
        ('L1', 'Licence 1'),
        ('M1', 'Master 1'),
    ]
    
    # Informations personnelles
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau_etude = models.CharField(max_length=50)
    etablissement_origine = models.CharField(max_length=200)
    concours_souhaite = models.CharField(max_length=2, choices=NIVEAU_CHOICES)
    date_inscription = models.DateTimeField(auto_now_add=True)
    
    # Documents à uploader
    extrait_naissance = models.FileField(upload_to='extraits/')
    certificat = models.FileField(upload_to='certificats/')
    lettre_motivation = models.FileField(upload_to='lettres/')
    diplome = models.FileField(upload_to='diplomes/')
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.concours_souhaite}"