from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from database.dbIdcours import dbIdcours
from database.models import Cours
from database.dbEtablissement import dbEtablissement
from database.dbProfesseur import dbProfesseur
from database.dbCours import dbCours
import datetime

# Create your views here.

def index(request):
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    schools = gest.returnAll()
    return render(request, 'cours/lister.html', {'school': schools})

def ajouter(request):
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    id = dbIdcours()
    idcours = id.returnAll()
    gest = dbEtablissement()
    etab = gest.returnAll()
    dbprof = dbProfesseur()
    prof = dbprof.returnAll()
    t = get_template('cours/ajouter.html')
    html = t.render(Context({'current_date': now,'idcours':idcours,'prof':prof,'etab':etab}))
    return HttpResponse(html)

def sauvegarder(request):
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()

    idcours = request.GET['idcours']
    prof = request.GET['professeur']
    nometab = request.GET['etablissement']
    titre = request.GET['titre']
    creditECTS = request.GET['creditECTS']
    public = request.GET['public']
    objectif = request.GET['objectif']
    description = request.GET['description']
    formatcours = request.GET['formatcours']
    prerequis = request.GET['prerequis']
    ressources = request.GET['ressources']
    evaluation = request.GET['evaluation']
    plan = request.GET['plan']

    id = dbIdcours()
    cours = id.returnAll()
    gest = dbEtablissement()
    etabli = gest.returnAll()
    dbprof = dbProfesseur()
    professeur = dbprof.returnAll()

    etab = dbCours()
    ecole = Cours(idcours=id.returnOne(id=idcours),professeur=dbprof.returnOne(id=prof),etablissement=gest.returnOne(id=nometab),titre=titre,creditECTS=creditECTS,public=public,objectif=objectif,description=description,plan=plan,formatcours=formatcours,prerequis=prerequis,ressources=ressources,evaluation=evaluation,date=now)

    if(not etab.isExist(idcours=id.returnOne(id=idcours),professeur=dbprof.returnOne(id=prof),etablissement=gest.returnOne(id=nometab),titre=titre)):
        if(not etab.save(ecole)):
            message = "Code cours ajouter !"
        else:
            message = "Code cours non ajouter."
    else:
        message = "le cours {} existe deja.".format(ecole.titre)
    return render(request, 'cours/ajouter.html',{'message': message,'idcours':cours,'prof':professeur,'etab':etabli})


def modifier(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
    idcours = dbIdcours()
    cours = idcours.returnOne(id)
    gest = dbEtablissement()
    etab = gest.returnAll()
    return render(request, 'cours/modifier.html',{'etab':cours,'school':etab})

def savemodification(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()

    idcours = request.GET['idcours']
    prof = request.GET['professeur']
    nometab = request.GET['etablissement']
    titre = request.GET['titre']
    creditECTS = request.GET['creditECTS']
    public = request.GET['public']
    objectif = request.GET['objectif']
    description = request.GET['description']
    formatcours = request.GET['formatcours']
    prerequis = request.GET['prerequis']
    ressources = request.GET['ressources']
    evaluation = request.GET['evaluation']
    plan = request.GET['plan']

    etab = dbIdcours()
    ecole = Cours(idcours=idcours,professeur=prof,etablissement=nometab,titre=titre,creditECTS=creditECTS,public=public,objectif=objectif,description=description,plan=plan,formatcours=formatcours,prerequis=prerequis,ressources=ressources,evaluation=evaluation)
    if(etab.modify(id=id,idcours=idcours,professeur=prof,etablissement=nometab,titre=titre,creditECTS=creditECTS,public=public,objectif=objectif,description=description,plan=plan,formatcours=formatcours,prerequis=prerequis,ressources=ressources,evaluation=evaluation,date=now)):
        message = "Code cours non modifier !"
    else:
        message = "Code cours modifier."
    return render(request, 'cours/modifier.html',{'message':message,'etab':ecole})

def supprimer(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbIdcours()
    etab = gest.returnOne(id)
    return render(request, 'cours/supprimer.html',{'etab':etab})

def savesuppression(request,id):
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbIdcours()
    etab = gest.returnOne(id=id)

    if(not etab==None):
        if(not gest.delete(id=id)):
            message = "Code cours effacee."
        else:
            message = "Code cours non effacee."
    else:
        message = "le code cours n'existe plus !"
    return render(request, 'cours/supprimer.html',{'message':message,'etab':etab})




