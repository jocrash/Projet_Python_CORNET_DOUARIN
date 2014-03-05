__author__ = 'joel CORNET'

import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from Admin.database.models import Users
from Admin.database.dbUsers import dbUsers

def login(request):
    users = dbUsers()
    user=users.returnAll()
    message = ''
    if 'username' in request.POST:
        for t in user :
            if request.POST['username'].__eq__(t.username) and request.POST['password'].__eq__(t.password):
               request.session['idsession'] = request.POST['username']
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
    return render(request, 'index/index.html',{'username':username})

def logout(request):
    del request.session['idsession']
    return redirect("/")

def create(request):
    if 'idsession' not in request.session:
            return redirect("/")
    return render(request, 'index/create.html')

def sauvegarder(request):
    if 'idsession' not in request.session:
        return redirect("/")
    now = datetime.datetime.now()
    users = dbUsers()
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    username = request.POST['username']
    password = request.POST['password']
    type = request.POST['type']

    utilisateur = Users(nom=nom,prenom=prenom,username=username,password=password,type=type,date=now)

    if(not users.isExist(username=username)):
        if(not users.save(utilisateur)):
            message = "Account created !"
        else:
            message = "Account not created."
    else:
        message = "le compte {} existe deja.".format(username)

    return render(request, 'index/create.html',{'message':message})


