__author__ = 'joel CORNET'

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

def login(request):
    t=('username','password')
    if 'username' in request.POST:
        if request.POST['username'].__eq__(t[0]) and request.POST['password'].__eq__(t[1]):
            request.session['idsession'] = request.POST['username']
        if 'idsession' in request.session:
            return redirect("/admin/")
    else:
        if 'idsession' in request.session:
            return redirect("/admin/")
    return render(request, 'login/login.html')

def index(request):
    if 'idsession' not in request.session:
            return redirect("/")
    return render(request, 'index/index.html')

def logout(request):
    del request.session['idsession']
    return redirect("/")
