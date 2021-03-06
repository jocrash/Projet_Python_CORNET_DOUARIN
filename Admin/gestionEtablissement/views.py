import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from Admin.database.dbEtablissement import dbEtablissement
from Admin.database.models import Etablissement


# Create your views here.

def index(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbEtablissement()
    schools = gest.returnAll()
    return render(request, 'etablissement/lister.html', {'school': schools,'username':username['idsession']})

def ajouter(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    t = get_template('etablissement/ajouter.html')
    html = t.render(Context({'current_date': now,'username':username['idsession']}))
    return HttpResponse(html)

def sauvegarder(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    nom = request.GET['nom']
    lieu = request.GET['lieu']
    etab = dbEtablissement()
    ecole = Etablissement(nom=nom,lieu=lieu,date=now)

    if(not etab.isExist(nom=nom,lieu=lieu)):
        if(not etab.save(ecole)):
            message = "Etablissement ajouter !"
        else:
            message = "Etablissemenet non ajouter."
    else:
        message = "l'etablissement {} existe deja.".format(nom)
    return render(request, 'etablissement/ajouter.html',{'message': message,'username':username['idsession']})


def modifier(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbEtablissement()
    etab = gest.returnOne(id)
    return render(request, 'etablissement/modifier.html',{'etab':etab,'username':username['idsession']})

def savemodification(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    nom = request.GET['nom']
    lieu = request.GET['lieu']
    gest = dbEtablissement()
    etab = Etablissement(nom=nom,lieu=lieu,date=now)
    if(gest.modify(id=id,nom=nom,lieu=lieu,date=now)):
        message = "Etablissement non modifier !"
    else:
        message = "Etablissement modifier."
    return render(request, 'etablissement/savemodification.html',{'message':message,'username':username['idsession']})

def supprimer(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbEtablissement()
    etab = gest.returnOne(id)
    return render(request, 'etablissement/supprimer.html',{'etab':etab,'username':username['idsession']})

def savesuppression(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbEtablissement()

    if(not gest.returnOne(id=id) == None):
        if(not gest.delete(id=id)):
            message = "Etablissement effacee."
        else:
            message = "Etablissement non effacee."
    else:
        message = "L'etablissemnt n'existe pas !"
    return render(request, 'etablissement/savesuppression.html',{'message':message,'username':username['idsession']})




