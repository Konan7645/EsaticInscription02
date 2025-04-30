from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import DetailView
from xhtml2pdf import pisa
from io import BytesIO
from .forms import InscriptionForm
from .models import Inscription

def accueil(request):
    return render(request, 'inscription/accueil.html')

def nouvelle_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            inscription = form.save()
            messages.success(request, "Votre inscription a été enregistrée avec succès !")
            return redirect('confirmation', pk=inscription.pk)
    else:
        form = InscriptionForm()
    
    return render(request, 'inscription/formulaire.html', {'form': form})

class ConfirmationView(DetailView):
    model = Inscription
    template_name = 'inscription/confirmation.html'
    context_object_name = 'inscription'

def generer_pdf(request, pk):
    # Récupérer l'inscription
    try:
        inscription = Inscription.objects.get(pk=pk)
    except Inscription.DoesNotExist:
        return HttpResponse("Inscription non trouvée", status=404)
    
    # Préparer le contexte pour le template
    context = {'inscription': inscription}
    
    # Charger le template
    template = get_template('inscription/pdf_template.html')
    html = template.render(context)
    
    # Créer un PDF à partir du HTML
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="inscription_{inscription.pk}.pdf"'
        return response
    
    return HttpResponse("Erreur lors de la génération du PDF", status=400)