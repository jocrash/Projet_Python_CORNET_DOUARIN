from django.shortcuts import render
__author__ = 'joel CORNET'

import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from Admin.database.models import Users
from Admin.database.dbUsers import dbUsers
from Admin.database.dbProfesseur import dbProfesseur
from Admin.database.dbCours import dbCours
from Admin.database.dbIdcours import dbIdcours
from Admin.database.dbEtablissement import dbEtablissement
from Admin.database.dbCours import Cours
from Admin.database.models import CVprof

# Create your views here.

username = ""

def login(request):
    users = dbUsers()
    user=users.returnAll()
    message = ''
    if 'username' in request.POST:
        for t in user :
            if request.POST['username'].__eq__(t.username) and request.POST['password'].__eq__(t.password):
               request.session['idsession'] = request.POST['username']
               username = request.POST['username']
               request.session['type'] = t.type
               if t.type == "Administrateur":
                   return redirect("/admin/")
               else:
                   return redirect("/professeur/")
            else:
                message = "Access denied"
        if 'idsession' in request.session:
            return redirect("/admin/")
    else:
        if 'idsession' in request.session:
            return redirect("/admin/")
    return render(request, 'login/login.html',{'message':message})

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
    return render(request, 'prof/lister.html', {'school': schools,'ecole':cours,'username':username['idsession']})

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
    return render(request, 'prof/details.html', {'school': schools,'username':username['idsession']})

def addcv(request):
    username = request.session
    gests = dbUsers()
    idprof = gests.returnOne(username['idsession'])
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProfesseur()
    prof = gest.returnOne(idprof.id)
    cv = gest.returnCV(idprof.id)
    return render(request,'prof/ajouterCV.html',{'etab':prof,'cv':cv,'username':username['idsession']})

def saveCV(request):
    username = request.session
    gests = dbUsers()
    idprof = gests.returnOne(username['idsession'])
    if 'idsession' not in request.session:
        return redirect("/")
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
    idprof = etab.returnOne(idprof)
    ecole = CVprof(idprof=idprof,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,formation=formation,etude=etude,experience=experience,langue=langue,reference=reference,date=now)

    if(not etab.isCVExist(idprof=idprof,nom=nom,prenom=prenom,cin=cin,sexe=sexe,telephone=telephone,email=email,formation=formation,etude=etude,experience=experience,langue=langue,reference=reference)):
        if(not etab.saveCV(ecole)):
            message = "CV ajouter !"
        else:
            message = "CV non ajouter."
    else:
        message = "le CV du professeur {} {} existe deja.".format(prenom,nom)
    return render(request, 'prof/saveCV.html',{'etab':ecole,'message': message,'username':username['idsession']})

def viewCV(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbProfesseur()
    gests = dbUsers()
    idprof = gests.returnOne(username['idsession'])
    prof = gest.returnOne(idprof.id)
    cv = gest.returnCV(idprof.id)
    if(not cv==None):
        message = ""
        find = True
    else:
        message = "Vous n'avez pas encore enregistrer votre CV. "
        find = False
    return render(request,'prof/cv.html',{'cv':cv, 'prof':prof,'message':message,'find':find,'username':username['idsession']})


def cours(request):
    username = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    gest = dbCours()
    schools = gest.returnAll()
    cours = []
    courProf = []
    gests = dbUsers()
    idprof = gests.returnOne(username['idsession'])
    for list in schools:
        if idprof.id == list.professeur.id:
            courProf.append(list)
    try:
        id = request.POST['cours']
        cours = gest.returnOne(id)
    except:
        pass
    return render(request, 'prof/listerCours.html', {'school': courProf,'ecole':cours,'username':username['idsession']})

def ajouter(request):
    now = datetime.datetime.now()
    if 'idsession' not in request.session:
        return redirect("/")
    try:
        cours = request.POST['cours']
        prerequis = request['prerequis']
        objectif = request.POST['objectif']
        description = request.POST['description']
        plan = request.POST['plan']
        formatcours = request.POST['formatcours']
        ressources = request.POST['ressources']
        evaluation = request.POST['evaluation']
        gest = dbCours()
        gest.fiche(id=cours,prerequis=prerequis,objectif=objectif,description=description,plan=plan,formatcours=formatcours,ressources=ressources,evaluation=evaluation,date=now)
    except:
        message = "Fiche non remplie."
    message = "Fiche enregistrer !"
    t = get_template('prof/cours.html')
    html = t.render(Context({'current_date': now,'message':message}))
    return HttpResponse(html)


# def ajouter(request):
#     if 'idsession' not in request.session:
#         return redirect("/")
#     now = datetime.datetime.now()
#     id = dbIdcours()
#     idcours = id.returnAll()
#     gest = dbEtablissement()
#     etab = gest.returnAll()
#     dbprof = dbProfesseur()
#     prof = dbprof.returnAll()
#     t = get_template('prof/cours.html')
#     html = t.render(Context({'current_date': now,'idcours':idcours,'prof':prof,'etab':etab}))
#     return HttpResponse(html)
#
# def sauvegarder(request):
#     if 'idsession' not in request.session:
#         return redirect("/")
#     now = datetime.datetime.now()
#
#     idcours = request.GET['idcours']
#     prof = request.GET['professeur']
#     nometab = request.GET['etablissement']
#     titre = request.GET['titre']
#     creditECTS = request.GET['creditECTS']
#     public = request.GET['public']
#     objectif = request.GET['objectif']
#     description = request.GET['description']
#     formatcours = request.GET['formatcours']
#     prerequis = request.GET['prerequis']
#     ressources = request.GET['ressources']
#     evaluation = request.GET['evaluation']
#     plan = request.GET['plan']
#
#     id = dbIdcours()
#     cours = id.returnAll()
#     gest = dbEtablissement()
#     etabli = gest.returnAll()
#     dbprof = dbProfesseur()
#     professeur = dbprof.returnAll()
#
#     etab = dbCours()
#     ecole = Cours(idcours=id.returnOne(id=idcours),professeur=dbprof.returnOne(id=prof),etablissement=gest.returnOne(id=nometab),titre=titre,creditECTS=creditECTS,public=public,objectif=objectif,description=description,plan=plan,formatcours=formatcours,prerequis=prerequis,ressources=ressources,evaluation=evaluation,date=now)
#
#     if(not etab.isExist(idcours=id.returnOne(id=idcours),professeur=dbprof.returnOne(id=prof),etablissement=gest.returnOne(id=nometab),titre=titre)):
#         if(not etab.save(ecole)):
#             message = "Code cours ajouter !"
#         else:
#             message = "Code cours non ajouter."
#     else:
#         message = "le cours {} existe deja.".format(ecole.titre)
#     return render(request, 'cours/ajouter.html',{'message': message,'idcours':cours,'prof':professeur,'etab':etabli})
