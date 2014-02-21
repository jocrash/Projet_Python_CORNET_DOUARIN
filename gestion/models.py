from django.db import models

# Create your models here.

class Etablissement(models.Model):
    nom = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)

class Programme(models.Model):
    domaine = models.CharField(max_length=10)
    mention = models.CharField(max_length=10)
    specialite = models.CharField(max_length=10)
    typecours = models.CharField(max_length=10)
    langue = models.CharField(max_length=10)

class Idcours(models.Model):
    etablissement = models.ForeignKey(Etablissement)
    annee = models.CharField(max_length=10)
    semestre = models.CharField(max_length=10)
    nomcours = models.CharField(max_length=100)


class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin = models.CharField(max_length=50)
    sexe = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

class Cours(models.Model):
    idcours = models.ForeignKey(Idcours)
    professeur = models.ForeignKey(Professeur)
    etablissement = models.ForeignKey(Etablissement)
    titre = models.CharField(max_length=200)
    creditECTS = models.IntegerField()
    public = models.CharField(max_length=100)
    prerequis = models.CharField(max_length=200)
    objectif = models.TextField()
    description = models.TextField()
    plan = models.TextField()
    formatcours = models.CharField(max_length=50)
    ressources = models.TextField()
    evaluation = models.TextField()


