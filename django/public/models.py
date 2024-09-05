from django.db import models
from django.contrib.auth.models import User
class Cle(models.Model):
    proprietaire = models.ForeignKey(User,on_delete=models.CASCADE)
    couleur = models.CharField(max_length=30)
    etat_pret = models.BooleanField()
    date_pret = models.DateField(null=True, blank=True)
    date_rendu = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.proprietaire
    class Meta:
        app_label="public"
class Garage(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    class Meta:
        app_label="public"
class Voiture(models.Model):
    marque = models.CharField(max_length=30)
    cle = models.ForeignKey(Cle, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    immatriculation = models.CharField(max_length=9)
    modele = models.CharField(max_length=30)
    annee_fabrication = models.IntegerField()
    def __str__(self):
        return self.marque+" "+self.immatriculation+" "+self.cle+" "+self.garage+" "+self.annee_fabrication
    class Meta:
        app_label="public"