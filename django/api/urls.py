from django.urls import path
from .views import *

urlpatterns = [
    path('', api_index, name='api_index'),
    path('voitures/', voiture_list_json, name='voiture_list_json'),
    path('cles/', cle_list_json, name='cle_list_json'),
    path('garages/', garage_list_json, name='garage_list_json'),
    path('users/', user_list_json, name='user_list_json'),
]
