from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'projetDjango.views.login', name='esih/login'),
    url(r'^admin/$', 'projetDjango.views.index', name='esih/index'),
    url(r'^logout/$', 'projetDjango.views.logout', name='esih/logout'),
    url(r'^admin/createAccount/$', 'projetDjango.views.create', name='esih/account'),
    url(r'^admin/createAccount/sauvegarder/$', 'projetDjango.views.sauvegarder', name='esih/account'),
    (r'^admin/esih/gestion_etablissement/', include('Admin.gestionEtablissement.urls')),
    (r'^admin/esih/gestion_programme/', include('Admin.gestionProgramme.urls')),
    (r'^admin/esih/gestion_Idcours/', include('Admin.gestionIdcours.urls')),
    (r'^admin/esih/gestion_professeur/', include('Admin.gestionProfesseur.urls')),
    (r'^admin/esih/gestion_cours/', include('Admin.gestionCours.urls')),
    url(r'^professeur/', include('professeur.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
