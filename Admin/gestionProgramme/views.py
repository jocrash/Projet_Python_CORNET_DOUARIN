import datetime

from Admin.database.dbProgramme import dbProgramme
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from Admin.database.models import Programme


# Create your views here.



def index(request):
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    programme = gest.returnAll()
    return render(request, 'programme/lister.html', {'school': programme})

def ajouter(request):
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    t = get_template('programme/ajouter.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def sauvegarder(request):
    if 'idsession' not in request.session:
        return redirect("/")
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
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/modifier.html',{'etab':etab})

def savemodification(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
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
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/supprimer.html',{'etab':etab})

def savesuppression(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
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




