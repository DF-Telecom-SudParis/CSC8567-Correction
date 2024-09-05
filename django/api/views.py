from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from public.models import Cle, Garage, Voiture
from django.contrib.auth.models import User

def voiture_list_json(request):
    voitures = Voiture.objects.all().values(
        'marque', 'modele', 'immatriculation', 'annee_fabrication',
        'cle__couleur', 'cle__etat_pret', 'cle__date_pret', 'cle__date_rendu',
        'garage__nom'
    )
    return JsonResponse(list(voitures), safe=False)

def cle_list_json(request):
    cles = Cle.objects.all().values(
        'proprietaire__username', 'couleur', 'etat_pret', 'date_pret', 'date_rendu'
    )
    return JsonResponse(list(cles), safe=False)

def garage_list_json(request):
    garages = Garage.objects.all().values('nom')
    return JsonResponse(list(garages), safe=False)

def user_list_json(request):
    users = User.objects.all().values('username', 'first_name', 'last_name', 'email', 'is_active')
    return JsonResponse(list(users), safe=False)

def api_index(request):
    data = {
        "message": "Bienvenue dans l'API de mon projet CSC8567 !",
        "endpoints": {
            "/api/voitures/": "Liste des Voitures",
            "/api/cles/": "Liste des Clés",
            "/api/garages/": "Liste des Garages",
            "/api/users/": "Liste des Utilisateurs"
        }
    }
    return JsonResponse(data)