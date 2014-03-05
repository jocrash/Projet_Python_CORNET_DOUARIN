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
    (r'^esih/gestion_etablissement/', include('gestionEtablissement.urls')),
    (r'^esih/gestion_programme/', include('gestionProgramme.urls')),
    (r'^esih/gestion_Idcours/', include('gestionIdcours.urls')),
    (r'^esih/gestion_professeur/', include('gestionProfesseur.urls')),
    (r'^esih/gestion_cours/', include('gestionCours.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
