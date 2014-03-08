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


def login(request):
    users = dbUsers()
    user=users.returnAll()
    message = ''
    if 'username' in request.POST:
        for t in user :
            if request.POST['username'].__eq__(t.username) and request.POST['password'].__eq__(t.password):
               request.session['idsession'] = request.POST['username']
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
    cours = gest.returnAll()
    info =  []
    for inf in cours:
        if inf.programme.mention == 'SI':
            info.append(inf.creditECTS)

    return render(request, 'index/index.html',{'info':info,'username':username['idsession']})

def logout(request):
    del request.session['idsession']
    return redirect("/")

def create(request):
    username = request.session
    if 'idsession' not in request.session:
            return redirect("/")
    gest = dbProfesseur()
    schools = gest.returnAll()
    return render(request, 'index/create.html',{'prof':schools,'username':username['idsession']})

def sauvegarder(request):
    user = request.session
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    users = dbUsers()
    gest = dbProfesseur()
    idprof = request.POST['idprof']
    username = request.POST['username']
    password = request.POST['password']
    type = request.POST['type']

    utilisateur = Users(professeur=gest.returnOne(idprof),username=username,password=password,type=type,date=now)

    if(not users.isExist(username=username)):
        if(not users.save(utilisateur)):
            message = "Account created !"
        else:
            message = "Account not created."
    else:
        message = "le compte {} existe deja.".format(username)

    return render(request, 'index/create.html',{'message':message,'username':user['idsession']})


