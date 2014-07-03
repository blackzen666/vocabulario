__author__ = 'noescobar'


from django.conf.urls import patterns, url
from views import *



urlpatterns = patterns('',
    url(r'^$', addVocabulario),
    url(r'^buscarInstituciones_ajax/$', Ajax().buscarInstituciones ),
    url(r'^buscarGrupos_ajax/$', Ajax().buscarGrupos),
    url(r'^buscarUsuarios_ajax/$', Ajax().buscarUsuarios),
    url(r'^buscarJuegos_ajax/$', Ajax().buscarJuegos),
    url(r'^buscarEtiquetas_ajax/$', Ajax().buscarEtiquetas),
)