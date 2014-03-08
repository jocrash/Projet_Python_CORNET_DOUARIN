import datetime

from Admin.database.dbProgramme import dbProgramme
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from Admin.database.models import Programme


# Create your views here.



def index(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    programme = gest.returnAll()
    return render(request, 'programme/lister.html', {'school': programme,'username':username['idsession']})

def ajouter(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    t = get_template('programme/ajouter.html')
    html = t.render(Context({'current_date': now,'username':username['idsession']}))
    return HttpResponse(html)

def sauvegarder(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    date = datetime.datetime.now()
    domaine = request.GET['domaine']
    mention = request.GET['mention']
    specialite = request.GET['specialite']
    typecours = request.GET['typecours']
    langue = request.GET['langue']
    codeprogramme = "{}-{}-{}-{}-{}".format(domaine,mention,specialite,typecours,langue)
    etab = dbProgramme()
    ecole = Programme(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue,codeprogramme=codeprogramme,date=date)

    if(not etab.isExist(domaine=domaine,mention=mention,specialite=specialite,typecours=typecours,langue=langue)):
        if(not etab.save(ecole)):
            message = "Programme ajouter !"
        else:
            message = "Programme non ajouter."
    else:
        message = "le programme {}-{}-{}-{}-{} existe deja.".format(domaine,mention,specialite,typecours,langue)
    return render(request, 'programme/ajouter.html',{'message': message,'username':username['idsession']})


def modifier(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/modifier.html',{'etab':etab,'username':username['idsession']})

def savemodification(request,id):
    username = request.session
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
    return render(request, 'programme/savemodification.html',{'message':message,'etab':etab,'username':username['idsession']})

def supprimer(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProgramme()
    etab = gest.returnOne(id)
    return render(request, 'programme/supprimer.html',{'etab':etab,'username':username['idsession']})

def savesuppression(request,id):
    username = request.session
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
    return render(request, 'programme/savesuppression.html',{'message':message,'etab':etab,'username':username['idsession']})




