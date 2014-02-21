from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from database.dbProgramme import dbProgramme
from database.models import Programme
import datetime

# Create your views here.



def index(request):
    gest = dbProgramme()
    programme = gest.returnAll()
    return render(request, 'programme/lister.html', {'school': programme})

def ajouter(request):
    now = datetime.datetime.now()
    t = get_template('programme/ajouter.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def sauvegarder(request):
    now = datetime.datetime.now()
    domaine = request.GET['domaine']
    mention = request.GET['mention']
    specialite = request.GET['specialite']
    typecours = request.GET['typecours']
    langue = request.GET['langue']
    etab = dbProgramme()
    ecole = Programme(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue,date=now)

    if(not etab.isExist(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue)):
        if(not etab.save(ecole)):
            message = "Programme ajouter !"
        else:
            message = "Programme non ajouter."
    else:
        message = "le programme {}-{}-{}-{}-{} existe deja.".format(domaine,mention,specialite,typecours,langue)
    return render(request, 'programme/ajouter.html',{'message': message})


def modifier(request,id):
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/modifier.html',{'etab':etab})

def savemodification(request,id):
    now = datetime.datetime.now()
    domaine = request.GET['domaine']
    mention = request.GET['mention']
    specialite = request.GET['specialite']
    typecours = request.GET['typecours']
    langue = request.GET['langue']
    gest = dbProgramme()
    etab = Programme(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue,date=now)
    if(gest.modify(id=id,domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue,date=now)):
        message = "programme non modifier !"
    else:
        message = "programme modifier."
    return render(request, 'programme/savemodification.html',{'message':message,'etab':etab})

def supprimer(request,id):
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/supprimer.html',{'etab':etab})

def savesuppression(request,id):
    gest = dbProgramme()
    etab = gest.returnOne(id=id)
    if(not etab == None):
        if(not gest.delete(id=id)):
            message = "programme effacee."
        else:
            message = "programme non effacee."
    else:
        message = "Le programme n'existe pas !"
    return render(request, 'programme/savesuppression.html',{'message':message,'etab':etab})




