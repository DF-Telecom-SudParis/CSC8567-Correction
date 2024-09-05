from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='public_index'),
    path('voitures/', liste_voiture_view, name='voiture_list'),
    path('users/', liste_user_view, name='user_list'),
    path('cles/', liste_cle_view, name='cle_list'),
    path('garages/', liste_garage_view, name='garage_list'),
]