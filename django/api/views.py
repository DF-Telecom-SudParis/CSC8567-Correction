from django.http import JsonResponse
from api.models import Voiture

def liste_voitures_api(request):
    cars = Voiture.objects.all().values('marque', 'cle', 'garage','immatriculation','modele','annee_fabrication')
    return JsonResponse(list(cars), safe=False)