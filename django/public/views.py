from django.shortcuts import render
from public.models import Voiture

def liste_voitures(request):
    voitures = Voiture.objects.all()
    return render(request, 'public/liste_voitures.html', {'voitures': voitures})
