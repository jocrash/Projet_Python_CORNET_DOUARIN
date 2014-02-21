import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from database.dbEtablissement import dbEtablissement
from database.models import Etablissement


# Create your views here.


def etablissement(request):
    now = datetime.datetime.now()
    t = get_template('ajouter.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def addetab(request):
    nom = request.GET['nom']
    lieu = request.GET['lieu']

    gest = dbEtablissement()
    school = Etablissement(nom=nom,lieu=lieu)

    if(gest.save(school)):
        message = "Etablissement non ajouter !"
    else:
        message = "Etablissement ajouter."

    t = get_template('ajouter.html')
    html = t.render(Context({'message':message}))
    #Etablissement(nom=nom,lieu=lieu).save()
    return HttpResponse(html)
    #return HttpResponseRedirect('listing/')

def listingetab(request):
    gest = dbEtablissement()
    schools = gest.returnAll()
    return render(request, 'lister.html', {'school': schools})

def modifyetab(request,id):
    gest = dbEtablissement()
    etab = gest.returnOne(id)
    return render(request, 'modifier.html',{'etab':etab})

def savemodification(request,id):
    nom = request.GET['nom']
    lieu = request.GET['lieu']
    gest = dbEtablissement()
    if(gest.modify(id=id,nom=nom,lieu=lieu)):
        message = "Etablissement non modifier !"
    else:
        message = "Etablissement modifier."
    t = get_template('modifier.html')
    html = t.render(Context({'message':message}))
    return HttpResponse(html)



