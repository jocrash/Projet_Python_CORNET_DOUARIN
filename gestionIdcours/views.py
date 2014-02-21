from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from database.dbIdcours import dbIdcours
from database.models import Idcours
from database.dbEtablissement import dbEtablissement
import datetime

# Create your views here.

def index(request):
    gest = dbIdcours()
    schools = gest.returnAll()
    return render(request, 'idcours/lister.html', {'school': schools})

def ajouter(request):
    now = datetime.datetime.now()
    gest = dbEtablissement()
    etab = gest.returnAll()
    t = get_template('idcours/ajouter.html')
    html = t.render(Context({'current_date': now,'etab':etab}))
    return HttpResponse(html)

def sauvegarder(request):
    now = datetime.datetime.now()
    gest = dbEtablissement()

    nometab = request.GET['etablissement']
    etabli = gest.searchEtab(nom=nometab)

    all = gest.returnAll()
    annee = request.GET['annee']
    semestre = request.GET['semestre']
    nomcours = request.GET['nomcours']
    etab = dbIdcours()
    code = "{}-{}{}-{}".format(etabli.nom,annee,semestre,nomcours)
    ecole = Idcours(etablissement=etabli,annee=annee,semestre=semestre,nomcours=nomcours,codecours=code,date=now)

    if(not etab.isExist(id_etablissement=etabli,annee=annee,semestre=semestre,nomcours=nomcours,codecours=code)):
        if(not etab.save(ecole)):
            message = "Code cours ajouter !"
        else:
            message = "Code cours non ajouter."
    else:
        message = "le Code cours {} existe deja.".format(code)
    return render(request, 'idcours/ajouter.html',{'message': message,'etab':all})


def modifier(request,id):
    idcours = dbIdcours()
    cours = idcours.returnOne(id)
    gest = dbEtablissement()
    etab = gest.returnAll()
    return render(request, 'idcours/modifier.html',{'etab':cours,'school':etab})

def savemodification(request,id):
    now = datetime.datetime.now()
    gest = dbEtablissement()
    nometab = request.GET['etablissement']
    etabli = gest.searchEtab(nom=nometab)
    all = gest.returnAll()
    annee = request.GET['annee']
    semestre = request.GET['semestre']
    nomcours = request.GET['nomcours']
    code = "{}-{}{}-{}".format(etabli.nom,annee,semestre,nomcours)
    etab = dbIdcours()
    ecole = Idcours(etablissement=etabli,annee=annee,semestre=semestre,nomcours=nomcours,codecours=code,date=now)
    if(etab.modify(id=id,id_etablissement=etabli,annee=annee,semestre=semestre,nomcours=nomcours,codecours=code,date=now)):
        message = "Code cours non modifier !"
    else:
        message = "Code cours modifier."
    return render(request, 'idcours/savemodification.html',{'message':message,'etab':ecole,'school':all})

def supprimer(request,id):
    gest = dbIdcours()
    etab = gest.returnOne(id)
    return render(request, 'idcours/supprimer.html',{'etab':etab})

def savesuppression(request,id):
    gest = dbIdcours()
    etab = gest.returnOne(id=id)

    if(not etab==None):
        if(not gest.delete(id=id)):
            message = "Code cours effacee."
        else:
            message = "Code cours non effacee."
    else:
        message = "le code cours n'existe plus !"
    return render(request, 'idcours/savesuppression.html',{'message':message,'etab':etab})




