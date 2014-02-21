from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('gestionProfesseur.views',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index'),
    url(r'^ajouter/','ajouter'),
    url(r'^sauvegarder/$','sauvegarder'),
    url(r'^modifier/(\d+)/$', 'modifier'),
    url(r'^modifier/sauvegarder/(\d+)/$', 'savemodification'),
    url(r'^suppression/(\d+)/$', 'supprimer'),
    url(r'^suppression/sauvegarder/(\d+)/$', 'savesuppression'),
    url(r'^CV/(\d+)/$', 'viewCV'),
    url(r'^ajouterCV/(\d+)/$', 'addcv'),
    url(r'^saveCV/(\d+)/$','saveCV'),


    #url(r'^listing/','listingetab'),
    #url(r'^modifier/(\d+)/$', 'modifyetab'),
    #url(r'^modifier/etablissement/(\d+)/$', 'savemodification'),

)
