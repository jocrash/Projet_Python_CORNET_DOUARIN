from django.db import models

# Create your models here.

class Etablissement(models.Model):
    nom = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)
    date = models.DateTimeField()

class Programme(models.Model):
    domaine = models.CharField(max_length=10)
    mention = models.CharField(max_length=10)
    specialite = models.CharField(max_length=10)
    typecours = models.CharField(max_length=10)
    langue = models.CharField(max_length=10)
    codeprogramme = models.CharField(max_length=500)
    date = models.DateTimeField()

class Idcours(models.Model):
    etablissement = models.ForeignKey(Etablissement)
    annee = models.CharField(max_length=10)
    semestre = models.CharField(max_length=10)
    nomcours = models.CharField(max_length=100)
    codecours = models.CharField(max_length=500)
    date = models.DateTimeField()

class Codecours_Programme(models.Model):
    idcours = models.ForeignKey(Idcours)
    programme = models.ForeignKey(Programme)

class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin = models.CharField(max_length=50)
    sexe = models.CharField(max_length=20)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField()

class CVprof(models.Model):
    idprof = models.ForeignKey(Professeur)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin = models.CharField(max_length=50)
    sexe = models.CharField(max_length=20)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    formation = models.TextField()
    etude = models.TextField()
    experience = models.TextField()
    langue = models.TextField()
    reference = models.CharField(max_length=500)
    date = models.DateTimeField()

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
    date = models.DateTimeField()

class Cours_programme(models.Model):
    cours = models.ForeignKey(Cours)
    programme = models.ForeignKey(Programme)

class Users(models.Model):
    professeur = models.ForeignKey(Professeur)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateTimeField()


