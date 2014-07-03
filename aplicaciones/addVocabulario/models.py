from __future__ import unicode_literals
from django.db import models

class Calificacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    class Meta:        
        db_table = 'contenido_idioma"."calificacion'

class Idioma(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    class Meta:
        db_table = 'geolocalizacion"."idioma'

class Estado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    class Meta:
        db_table = 'contenido_idioma"."estado'

class Etiqueta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    idioma = models.ForeignKey('Idioma')
    estado = models.ForeignKey(Estado, blank=True, null=True)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta'


class Palabra(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    idioma = models.ForeignKey('Idioma')
    estado = models.ForeignKey(Estado, blank=True, null=True)
    class Meta:
        db_table = 'contenido_idioma"."palabra'


class Frase(models.Model):
    id = models.IntegerField(primary_key=True)
    clausula = models.CharField(unique=True, max_length=255)
    calificacion = models.ForeignKey(Calificacion)
    idioma = models.ForeignKey('Idioma')
    class Meta:
        db_table = 'contenido_idioma"."frase'




class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    class Meta:
        db_table = 'geolocalizacion"."pais'




class Departamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    pais = models.ForeignKey('Pais')
    class Meta:
        db_table = 'geolocalizacion"."departamento'



class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    departamento = models.ForeignKey('Departamento')
    departamento_pais_id = models.IntegerField()
    class Meta:
        db_table = 'geolocalizacion"."ciudad'

class Direccion(models.Model):
    id = models.IntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=45, blank=True)
    ciudad = models.ForeignKey(Ciudad)
    ciudad_departamento_id = models.IntegerField()
    ciudad_departamento_pais_id = models.IntegerField()
    class Meta:
        db_table = 'geolocalizacion"."direccion'


class Telefono(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.CharField(unique=True, max_length=15, blank=True)
    usuario = models.ForeignKey('Usuario', blank=True, null=True, related_name = 'usuario')
    class Meta:
        db_table = 'datos_usuario"."telefono'


class Institucion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    limite_de_grupos = models.IntegerField(blank=True, null=True)
    limite_de_alumnos = models.IntegerField(blank=True, null=True)
    tiene_limite_de_alumnos = models.NullBooleanField()
    habilitado = models.NullBooleanField()
    direccion = models.ForeignKey('Direccion', blank=True, null=True)
    class Meta:
        db_table = 'organizacion"."institucion'




class Juego(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    vista_previa = models.CharField(max_length=70)
    ruta = models.CharField(max_length=70)
    class Meta:
        db_table = 'juegos"."juego'





class Skin(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    vista_previa = models.CharField(max_length=70)
    ruta = models.CharField(max_length=70)
    juego = models.ForeignKey(Juego)
    class Meta:
        db_table = 'juegos"."skin'

class SkinTieneEtiqueta(models.Model):
    skin = models.ForeignKey(Skin)
    etiqueta = models.ForeignKey('Etiqueta')
    estado = models.ForeignKey('Estado')
    class Meta:
        db_table = 'juegos"."skin_tiene_etiqueta'



class InstitucionTieneEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta, primary_key= True)
    institucion = models.ForeignKey('Institucion', primary_key= True)
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."institucion_tiene_etiqueta'




class Grupo(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    nombre = models.CharField(max_length=45)
    limite_de_alumnos = models.IntegerField(blank=True, null=True)
    tiene_limite_de_alumnos = models.NullBooleanField()
    habilitado = models.NullBooleanField()
    direccion = models.ForeignKey('Direccion', blank=True, null=True)
    institucion = models.ForeignKey('Institucion')
    class Meta:
        db_table = 'organizacion"."grupo'



class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45, blank=True)
    fecha_de_nacimiento = models.DateTimeField()
    telefono = models.ForeignKey(Telefono, blank=True, null=True, related_name = 'telefono')
    direccion = models.ForeignKey('Direccion', blank=True, null=True)
    class Meta:
        db_table = 'datos_usuario"."usuario'


class Correo(models.Model):
    correo = models.CharField(unique=True, max_length=80, primary_key= True)
    usuario = models.ForeignKey('Usuario')
    class Meta:
        db_table = 'datos_usuario"."correo'


class Perfil(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    class Meta:
        db_table = 'datos_usuario"."perfil'


class UsuarioHablaIdioma(models.Model):
    usuario = models.ForeignKey(Usuario,primary_key=True)
    idioma = models.ForeignKey('Idioma',primary_key=True)
    class Meta:
        db_table = 'datos_usuario"."usuario_habla_idioma'

class UsuarioTienePerfil(models.Model):
    usuario = models.ForeignKey(Usuario)
    perfil = models.ForeignKey(Perfil)
    class Meta:
        db_table = 'datos_usuario"."usuario_tiene_perfil'


class DefinicionPalabra(models.Model):
    palabra = models.ForeignKey('Palabra', primary_key=True)
    definicion = models.CharField(max_length=45)
    idioma = models.ForeignKey('Idioma')
    class Meta:
        db_table = 'contenido_idioma"."definicion_palabra'


class EtiquetaHabilitada(models.Model):
    grupo = models.ForeignKey(Grupo, primary_key= True)
    usuario = models.ForeignKey(Usuario, primary_key= True)
    etiqueta = models.ForeignKey(Etiqueta)
    idioma = models.ForeignKey('Idioma')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_habilitada'


class PalabraHabilitada(models.Model):
    grupo = models.ForeignKey(EtiquetaHabilitada)
    usuario_id = models.IntegerField()
    etiqueta_id = models.IntegerField()
    palabra = models.ForeignKey(Palabra)
    idioma_id = models.IntegerField()
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."palabra_habilitada'


class DefinicionHabilitada(models.Model):
    grupo = models.ForeignKey('PalabraHabilitada')
    usuario_id = models.IntegerField()
    etiqueta_id = models.IntegerField()
    palabra_id = models.IntegerField()
    idioma_id = models.IntegerField()
    definicion = models.ForeignKey('DefinicionPalabra')
    estado = models.ForeignKey('Estado')
    class Meta:
        db_table = 'contenido_idioma"."definicion_habilitada'


class EstructuraFrase(models.Model):
    frase = models.ForeignKey('Frase', primary_key=True)
    palabras = models.CharField(unique=True, max_length=500)
    class Meta:
        db_table = 'contenido_idioma"."estructura_frase'



class EstructuraFraseEtiquetas(models.Model):
    frase = models.ForeignKey('Frase')
    etiquetas = models.CharField(max_length=500)
    class Meta:
        db_table = 'contenido_idioma"."estructura_frase_etiquetas'


class EtiquetaTieneEtiqueta(models.Model):
    etiqueta_id_index = models.ForeignKey(Etiqueta, db_column='etiqueta_id_index', related_name = 'id_etiqueta',primary_key= True)
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_etiqueta'



class EtiquetaTieneFrase(models.Model):
    frase = models.ForeignKey('Frase')
    etiqueta = models.ForeignKey(Etiqueta)
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_frase'


class Imagen(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:
        db_table = 'multimedia"."imagen'


class ImagenHabilitada(models.Model):
    grupo = models.ForeignKey('PalabraHabilitada')
    usuario_id = models.IntegerField()
    etiqueta_id = models.IntegerField()
    palabra_id = models.IntegerField()
    idioma_id = models.IntegerField()
    imagen = models.ForeignKey('Imagen')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."imagen_habilitada'


class Sonido(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:
        db_table = 'multimedia"."sonido'



class SonidoHabilitado(models.Model):
    grupo = models.ForeignKey(PalabraHabilitada)
    usuario_id = models.IntegerField()
    etiqueta_id = models.IntegerField()
    palabra_id = models.IntegerField()
    idioma_id = models.IntegerField()
    sonido = models.ForeignKey('Sonido')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."sonido_habilitado'





class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ruta = models.CharField(unique=True, max_length=45, blank=True)
    class Meta:
        db_table = 'multimedia"."video'



class EtiquetaTieneImagen(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    imagen = models.ForeignKey('Imagen')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_imagen'


class EtiquetaTieneSonido(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    sonido = models.ForeignKey('Sonido')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_sonido'



class EtiquetaTieneVideo(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    video = models.ForeignKey('Video')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_video'



class TipoEtiqueta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True)
    idioma = models.ForeignKey('Idioma')
    class Meta:
        db_table = 'contenido_idioma"."tipo_etiqueta'


class EtiquetaTieneTipoEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    tipo_etiqueta = models.ForeignKey('TipoEtiqueta')
    class Meta:
        db_table = 'contenido_idioma"."etiqueta_tiene_tipo_etiqueta'



class FraseHabilitada(models.Model):
    frase = models.ForeignKey(Frase)
    grupo = models.ForeignKey('PalabraHabilitada')
    usuario_id = models.IntegerField()
    etiqueta_id = models.IntegerField()
    palabra_id = models.IntegerField()
    idioma_id = models.IntegerField()
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."frase_habilitada'


class FraseRespondeFrase(models.Model):
    frase_respuesta = models.ForeignKey(Frase, db_column='frase_respuesta', related_name = 'frase_pregunta')
    frase_pregunta = models.ForeignKey(Frase, db_column='frase_pregunta')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."frase_responde_frase'



class FraseTieneImagen(models.Model):
    frase = models.ForeignKey(Frase)
    imagen = models.ForeignKey('Imagen')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."frase_tiene_imagen'



class FraseTieneSonido(models.Model):
    frase = models.ForeignKey(Frase)
    sonido = models.ForeignKey('Sonido')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'frase_tiene_sonido'


class FraseTieneVideo(models.Model):
    frase = models.ForeignKey(Frase)
    video = models.ForeignKey('Video')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."frase_tiene_video'



class GrupoTieneEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    grupo = models.ForeignKey('Grupo')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."grupo_tiene_etiqueta'


class PalabraTieneEtiqueta(models.Model):
    palabra = models.ForeignKey(Palabra, primary_key=True)
    etiqueta = models.ForeignKey(Etiqueta, primary_key=True)
    estado = models.ForeignKey(Estado, primary_key=True)
    class Meta:
        db_table = 'contenido_idioma"."palabra_tiene_etiqueta'


class PalabraTieneImagen(models.Model):
    palabra = models.ForeignKey(Palabra)
    imagen = models.ForeignKey('Imagen')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."palabra_tiene_imagen'

class PalabraTieneSonido(models.Model):
    palabra = models.ForeignKey(Palabra)
    sonido = models.ForeignKey('Sonido')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."palabra_tiene_sonido'

class PalabraTieneVideo(models.Model):
    palabra = models.ForeignKey(Palabra)
    video = models.ForeignKey('Video')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."palabra_tiene_video'


class UsuarioDuenoDefinicionPalabra(models.Model):
    etiqueta = models.ForeignKey(Etiqueta)
    definicion_palabra = models.ForeignKey(DefinicionPalabra)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_definicion_palabra'



class UsuarioDuenoEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,related_name = 'etiquetaprincipal',primary_key= True)
    etiqueta_id1 = models.ForeignKey(Etiqueta, db_column='etiqueta_id1',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_etiqueta'


class UsuarioDuenoFrase(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    frase = models.ForeignKey(Frase,primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_frase'

class UsuarioDuenoImagen(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    imagen = models.ForeignKey('Imagen',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_imagen'


class UsuarioDuenoJuego(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    juego = models.ForeignKey('Juego',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_juego'



class UsuarioDuenoPalabra(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    palabra = models.ForeignKey(Palabra,primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_palabra'


class UsuarioDuenoSonido(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    sonido = models.ForeignKey('Sonido',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_sonido'


class UsuarioDuenoVideo(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    video = models.ForeignKey('Video',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_dueno_video'



class UsuarioTieneEtiqueta(models.Model):
    etiqueta = models.ForeignKey(Etiqueta,primary_key= True)
    usuario = models.ForeignKey('Usuario',primary_key= True)
    class Meta:
        db_table = 'contenido_idioma"."usuario_tiene_etiqueta'


class VideoHabilitado(models.Model):
    grupo = models.ForeignKey(PalabraHabilitada)
    usuario_id = models.ForeignKey('Usuario')
    etiqueta_id = models.ForeignKey('Etiqueta')
    palabra_id = models.ForeignKey('Palabra')
    idioma_id = models.ForeignKey('Idioma')
    video = models.ForeignKey('Video')
    estado = models.ForeignKey(Estado)
    class Meta:
        db_table = 'contenido_idioma"."video_habilitado'




class GrupoAdministradoUsuario(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('Usuario')
    class Meta:
        db_table = 'organizacion"."grupo_administrado_usuario'

class GrupoTieneAlumno(models.Model):
    grupo = models.ForeignKey(Grupo, primary_key= True)
    usuario = models.ForeignKey('Usuario', primary_key= True)
    habilitado = models.NullBooleanField()
    class Meta:
        db_table = 'organizacion"."grupo_tiene_alumno'

class GrupoTieneProfesor(models.Model):
    grupo = models.ForeignKey(Grupo)
    usuario = models.ForeignKey('Usuario')
    habilitado = models.NullBooleanField()
    class Meta:
        db_table = 'organizacion"."grupo_tiene_profesor'



class InstitucionAdministradaUsuario(models.Model):
    institucion = models.ForeignKey(Institucion, primary_key=True)
    usuario = models.ForeignKey('Usuario', primary_key= True)
    class Meta:
        db_table = 'organizacion"."institucion_administrada_usuario'

class UsuarioAdministraUsuario(models.Model):
    usuario_admin = models.ForeignKey('Usuario', related_name = 'usuarioAdministrador')
    usuario = models.ForeignKey('Usuario')
    class Meta:
        db_table = 'organizacion"."usuario_administra_usuario'




class Cuenta(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    psswd = models.CharField(max_length=45)
    correo_correo = models.ForeignKey('Correo', db_column='correo_correo', blank=True, null=True, to_field='correo')
    class Meta:
        db_table = 'seguridad"."cuenta'

class CuentaTienePermiso(models.Model):
    cuenta_usuario = models.ForeignKey(Cuenta, db_column='cuenta_usuario', primary_key= True)
    permiso = models.ForeignKey('Permiso')
    class Meta:
        db_table = 'seguridad"."cuenta_tiene_permiso'

class Permiso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    class Meta:
        db_table = 'seguridad"."permiso'

