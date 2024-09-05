from django.urls import path

from api.views import liste_voitures_api

urlpatterns = [
    path("", liste_voitures_api, name="liste_voitures_api"),
]