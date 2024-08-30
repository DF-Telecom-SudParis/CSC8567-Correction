from django.urls import path
from public.views import liste_voitures

urlpatterns = [
    path('voitures/', liste_voitures, name='liste_voitures'),
]
