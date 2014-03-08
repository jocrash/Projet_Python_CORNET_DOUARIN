from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('professeur.views',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index'),
    # url(r'^profile/(\d+)/','viewCV'),
    url(r'^cours/remplirFiche/','ajouter'),
    url(r'^cours/(\d+)/','details'),
    url(r'^fiche/','cours'),
    url(r'^monCV/','viewCV'),
    url(r'^CV/','addcv'),


)
