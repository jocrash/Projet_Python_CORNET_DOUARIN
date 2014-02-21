from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from database.dbProfesseur import dbProfesseur
from database.models import Professeur
from database.models import CVprof
import datetime

# Create your views here.

def index(request):
    gest = dbProfesseur()
    schools = gest.returnAll()
    return render(request, 'professeur/lister.html', {'school': schools})

def ajouter(request):
    now = datetime.datetime.now()
    t = get_template('professeur/ajouter.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def sauvegarder(request):
    now = datetime.datetime.now()
    nom = request.GET['nom']
    prenom = request.GET['prenom']
    sexe = request.GET['sexe']
    cin = request.GET['cin']
    telephone = request.GET['telephone']
    email = request.GET['email']
    etab = dbProfesseur()
    ecole = Professeur(nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,date=now)

    if(not etab.isExist(nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email)):
        if(not etab.save(ecole)):
            message = "professeur ajouter !"
        else:
            message = "professeur non ajouter."
    else:
        message = "le professeur {} {} existe deja.".format(prenom,nom)
    return render(request, 'professeur/ajouter.html',{'etab':ecole,'message': message})


def modifier(request,id):
    gest = dbProfesseur()
    etab = gest.returnOne(id)
    return render(request, 'professeur/modifier.html',{'etab':etab})

def savemodification(request,id):
    now = datetime.datetime.now()
    nom = request.GET['nom']
    prenom = request.GET['prenom']
    sexe = request.GET['sexe']
    cin = request.GET['cin']
    telephone = request.GET['telephone']
    email = request.GET['email']
    gest = dbProfesseur()
    etab = Professeur(nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,date=now)
    if(gest.modify(id=id,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,date=now)):
        message = "professeur non modifier !"
    else:
        message = "professeur modifier."
    return render(request, 'professeur/savemodification.html',{'message':message,'etab':etab})

def supprimer(request,id):
    gest = dbProfesseur()
    etab = gest.returnOne(id)
    return render(request, 'professeur/supprimer.html',{'etab':etab})

def savesuppression(request,id):
    gest = dbProfesseur()
    if(not gest.delete(id=id)):
        message = "professeur effacee."
    else:
        message = "professeur non effacee."
    return render(request, 'professeur/savesuppression.html',{'message':message})

#### GESTION CV DU PROFESSEUR ####

def addcv(request,id):
    gest = dbProfesseur()
    prof = gest.returnOne(id)
    cv = gest.returnCV(id)
    return render(request,'professeur/ajouterCV.html',{'etab':prof,'cv':cv})

def saveCV(request,id):
    now = datetime.datetime.now()
    nom = request.GET['nom']
    prenom = request.GET['prenom']
    sexe = request.GET['sexe']
    cin = request.GET['cin']
    telephone = request.GET['telephone']
    email = request.GET['email']
    formation = request.GET['formation']
    etude = request.GET['etude']
    experience = request.GET['experience']
    langue = request.GET['langue']
    reference = request.GET['reference']

    etab = dbProfesseur()
    idprof = etab.returnOne(id)
    ecole = CVprof(idprof=idprof,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,formation=formation,etude=etude,experience=experience,langue=langue,reference=reference,date=now)

    if(not etab.isCVExist(idprof=idprof,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,formation=formation,etude=etude,experience=experience,langue=langue,reference=reference)):
        if(not etab.saveCV(ecole)):
            message = "CV ajouter !"
        else:
            message = "CV non ajouter."
    else:
        message = "le CV du professeur {} {} existe deja.".format(prenom,nom)
    return render(request, 'professeur/saveCV.html',{'etab':ecole,'message': message})


def viewCV(request,id):
    gest = dbProfesseur()
    prof = gest.returnOne(id)
    cv = gest.returnCV(id)
    if(not cv==None):
        message = ""
        find = True
    else:
        message = "le professeur {} {} n'a pas de CV.".format(prof.prenom,prof.nom)
        find = False
    return render(request,'professeur/cv.html',{'cv':cv, 'prof':prof,'message':message,'find':find})






