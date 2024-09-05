from django.shortcuts import render
from public.models import *

def home(request):
    return render(request, 'home.html')

def liste_voiture_view(request):
    voitures = Voiture.objects.all()
    return render(request, 'public/liste_voitures.html', {'voitures': voitures})

def liste_cle_view(request):
    cles = Cle.objects.all()
    return render(request, 'public/liste_cles.html',{'cles': cles})

def liste_garage_view(request):
    garages = Garage.objects.all()
    return render(request, 'public/liste_garages.html',{'garages': garages})

def liste_user_view(request):
    users = User.objects.all()
    return render(request,'public/liste_users.html',{'users': users})

def index_view(request):
    return render(request,'public/index.html')