from django.urls import path
from public.views import liste_voitures

urlpatterns = [
    path('', liste_voitures, name='liste_voitures'),
]
