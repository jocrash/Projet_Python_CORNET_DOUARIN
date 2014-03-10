from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('professeur.views',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index'),
    # url(r'^profile/(\d+)/','viewCV'),
    # url(r'^cours/','cours'),
    # url(r'^cours/(\d+)/','ajouter'),


)
