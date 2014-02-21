from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('gestion.views',
    # Examples:
    # url(r'^$', 'projetDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Enregistrement/','etablissement'),
    url(r'^etablissement/','addetab'),
    url(r'^listing/','listingetab'),
    url(r'^modifier/(\d+)/$', 'modifyetab'),
    url(r'^modifier/etablissement/(\d+)/$', 'savemodification'),

)
