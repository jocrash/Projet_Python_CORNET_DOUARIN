from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Admin.gestionCours.views',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index'),
    url(r'^/(\d+)$','getCours'),
    url(r'^ajouter/','ajouter'),
    url(r'^sauvegarder/','sauvegarder'),
    url(r'^details/(\d+)/$','details'),
    url(r'^modifier/(\d+)/$', 'modifier'),
    url(r'^modifier/sauvegarder/(\d+)/$', 'savemodification'),
    url(r'^suppression/(\d+)/$', 'supprimer'),
    url(r'^suppression/sauvegarder/(\d+)/$', 'savesuppression'),

    #url(r'^listing/','listingetab'),
    #url(r'^modifier/(\d+)/$', 'modifyetab'),
    #url(r'^modifier/etablissement/(\d+)/$', 'savemodification'),

)
