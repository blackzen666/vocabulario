from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from models import *
from django.views.generic import TemplateView
from django.core import serializers
import json
from django.db.models import Q
from PalabrasFrasesEtiqueta import *

def addVocabulario(request):
    usuario = Usuario.objects.filter(pk = 1)
    administradas = []
    if len(usuario) == 0:
        usuario = None
    if None != usuario:
        if len(usuario) > 0:
            usuario = usuario[0]
            administradas = InstitucionAdministradaUsuario.objects.filter(usuario_id__exact =usuario.id)
    instituciones = Institucion.objects.filter(id__in = administradas.values('institucion_id'))
    return render_to_response('addVocabulario/vocabularios.html', {'NUMBERS': range(0,3), 'INSTITUCIONES' : instituciones}, RequestContext(request))#{'current_datetime': now})




class Ajax(TemplateView):


    def buscarInstituciones(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(pk = 1)
        institucionesAdministradas = InstitucionAdministradaUsuario.objects.filter(usuario_id = usuario.id)
        instituciones = Institucion.objects.filter(id__in = institucionesAdministradas.values('institucion') )
        instituciones = serializers.serialize('json',instituciones)
        return HttpResponse(instituciones, mimetype = 'application/json')


    def buscarGrupos(self,request,*args,**kwargs):
        usuario = Usuario.objects.get(pk = 1)
        institucionID = request.GET['institucion']
        instituciones = InstitucionAdministradaUsuario.objects.filter(institucion =  institucionID)
        if instituciones.filter(usuario_id = usuario.id):
            grupos = Grupo.objects.filter(institucion__exact = instituciones.values('institucion'))
            if grupos.count() > 0:
                grupos = serializers.serialize('json',grupos)
                return HttpResponse(grupos, mimetype = 'application/json')
            else:
                mensaje = 'no se han encontrado grupos a cargo de esta institucion'
                return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')
        else:
            return HttpResponse(json.dumps('Usted no tiene permiso sobre esta institucion'), mimetype = 'application/json')



    def buscarUsuarios(self,request,*args,**kwargs):
        mensaje = 'problemas en la autenticacion porfavor asegurese de que todo este correcto'
        usuario = Usuario.objects.get(pk = 1)
        grupoID = request.GET['grupo']
        grupo = get_or_none(Grupo, id = grupoID)
        print grupo
        if grupo != None:
            administrada = get_or_none(InstitucionAdministradaUsuario,institucion_id = grupo.institucion_id)
            print administrada
            if administrada != None:
                if(administrada.usuario_id == usuario.id):
                    grupoUsuarios = GrupoTieneAlumno.objects.filter(grupo = grupo)
                    usuarios = Usuario.objects.filter(id__in = grupoUsuarios.values('usuario_id'))
                    usuarios = serializers.serialize('json',usuarios)
                    return HttpResponse(usuarios , mimetype = 'application/json')
                else:
                    return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')
            else:
                return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')
        else:
            return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')

    def buscarJuegos(self,request,*args,**kwargs):
        usuario = Usuario.objects.get(pk = 1)
        institucionID = request.GET['institucion']
        grupoID = request.GET['grupo']
        query = (Q(institucion_id = institucionID) & Q(usuario_id =usuario.id))
        instucionAdmin =InstitucionAdministradaUsuario.objects.filter(query).count()
        if(instucionAdmin == 1):
            query = (Q(id = grupoID) & Q(institucion_id = institucionID))
            grupo = Grupo.objects.filter(query).count()
            if(grupo == 1):
                juegos = Juego.objects.all()
                if(juegos.count() == 0):
                    mensaje = 'No se a encontrado ningun juego'
                    return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')
                else:
                    juegos = serializers.serialize('json',juegos)
                    return HttpResponse(juegos, mimetype = 'application/json')
        else:
            mensaje = 'Usted no es el usuario correspondiente, porfavor loguearse nuevamente'
            return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')


    def buscarEtiquetas(self,request,*args,**kwargs):
        usuario = Usuario.objects.get(pk = 1)
        institucionID = request.GET['institucion']
        query = (Q(institucion_id = institucionID) & Q(usuario_id =usuario.id))
        instucionAdmin =InstitucionAdministradaUsuario.objects.filter(query).count()
        if(instucionAdmin == 1):
            print institucionID
            etiquetas = PalabrasFrasesEtiqueta().getEtiquetasPublicOwner(dueno= institucionID, tipo = 'institucion')
            if etiquetas:
                etiquetas = serializers.serialize('json',etiquetas)
                return HttpResponse(etiquetas, mimetype = 'application/json')
            else:
                mensaje = 'No se a encontrado ninguna Etiqueta'
                return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')
        else:
            mensaje = 'Usted no es el usuario correspondiente, porfavor loguearse nuevamente'
            return HttpResponse(json.dumps(mensaje), mimetype = 'application/json')