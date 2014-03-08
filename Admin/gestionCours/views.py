import datetime

from Admin.database.dbCours import dbCours
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from Admin.database.dbIdcours import dbIdcours
from Admin.database.models import Cours
from Admin.database.dbEtablissement import dbEtablissement
from Admin.database.dbProfesseur import dbProfesseur


# Create your views here.

def index(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    schools = gest.returnAll()
    cours = []
    try:
        id = request.POST['cours']
        cours = gest.returnOne(id)
    except:
        pass
    return render(request, 'cours/lister.html', {'school': schools,'ecole':cours,'username':username['idsession']})

def ajouter(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    id = dbIdcours()
    idcours = id.returnAll()
    dico = {}
    for ele in idcours:
        dico = {ele.id:ele.nomcours}
    gest = dbEtablissement()
    etab = gest.returnAll()
    dbprof = dbProfesseur()
    prof = dbprof.returnAll()
    t = get_template('cours/ajouter.html')
    html = t.render(Context({'current_date': now,'idcours':idcours,'prof':prof,'etab':etab,'dico':dico,'username':username['idsession']}))
    return HttpResponse(html)

def sauvegarder(request):
    username = request.session
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
    return render(request, 'cours/ajouter.html',{'message': message,'idcours':cours,'prof':professeur,'etab':etabli,'username':username['idsession']})


def modifier(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    idcours = dbCours()
    cours = idcours.returnOne(id)
    gest = dbEtablissement()
    etab = gest.returnAll()
    prof = dbProfesseur()
    mr = prof.returnAll()
    return render(request, 'cours/modifier.html',{'etab':cours,'school':etab,'prof':mr,'username':username['idsession']})

def savemodification(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()

    cod = request.GET['idcours']
    code = dbIdcours()
    idcours = code.returnID(codecours=cod)
    p = request.GET['professeur']
    pro = dbProfesseur()
    prof = pro.returnOne(id=p)
    nomab = request.GET['etablissement']
    tab = dbEtablissement()
    etablissement = tab.returnOne(id=nomab)
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

    etab = dbCours()
    if(etab.modify(id=id,idcours=idcours,professeur=prof,etablissement=etablissement,titre=titre,creditECTS=creditECTS,public=public,objectif=objectif,description=description,plan=plan,formatcours=formatcours,prerequis=prerequis,ressources=ressources,evaluation=evaluation,date=now)):
        message = "Code cours non modifier !"
    else:
        message = "Code cours modifier."
    return render(request, 'cours/savemodification.html',{'message':message,'username':username['idsession']})

def supprimer(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    etab = gest.returnOne(id)
    return render(request, 'cours/supprimer.html',{'etab':etab,'username':username['idsession']})

def savesuppression(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    etab = gest.returnOne(id=id)

    if(not etab==None):
        if(not gest.delete(id=id)):
            message = "Cours supprimer."
        else:
            message = "Cours non supprimer."
    else:
        message = "le cours n'existe plus !"
    return render(request, 'cours/savesuppression.html',{'message':message,'username':username['idsession']})

def getCours(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")

    gest = dbCours()
    etab = gest.returnOne(id)
    return render(request, 'cours/lister.html',{'etab':etab,'username':username['idsession']})

def details(request,id):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    schools = gest.returnOne(id=id)
    cours = []
    # try:
    #     id = request.POST['cours']
    #     cours = gest.returnOne(id)
    # except:
    #     pass
    return render(request, 'cours/details.html', {'school': schools,'username':username['idsession']})




