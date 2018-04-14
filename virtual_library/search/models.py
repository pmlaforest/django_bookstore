from django.db import models

# Create your models here.

class Livre(models.Model):
    livre_nom = models.CharField(max_length=100)
    livre_auteur = models.CharField(max_length=100)
    livre_annee = models.CharField(max_length=4)
    livre_pages = models.IntegerField()