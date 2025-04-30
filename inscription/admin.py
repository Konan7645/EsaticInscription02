from django.contrib import admin
from .models import Inscription

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'concours_souhaite', 'date_inscription')
    search_fields = ('nom', 'prenom', 'etablissement_origine')
    list_filter = ('concours_souhaite', 'date_inscription')
    date_hierarchy = 'date_inscription'