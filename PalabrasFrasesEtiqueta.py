from aplicaciones.addVocabulario.models import *
from django.db.models import Q
import random
import operator


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None




class PalabrasFrasesEtiqueta(object):
    dbMultimedia = 'Multimedia'
    dbGeolocalizacion = 'Geolocalizacion'


    def getPalabras(self, order=(False, "")):
        palabras = Palabra.objects.all()

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasAleatoria(self, limite=None, order=(False, "")):
        count = Palabra.objects.all().count()

        if (not (limite == None)):
            if (count >= limite):
                slice = random.random() * (count - limite)
                palabras = Palabra.objects.all()[slice: slice + limite]
            else:
                palabras = Palabra.objects.all()
        else:
            palabras = Palabra.objects.all()

        return palabras

    def getPalabraId(self, id):
        palabras = Palabra.objects.filter(pk=id)
        return palabras

    def getPalabrasNombre(self, nombre):
        palabras = Palabra.objects.filter(nombre__iexact=nombre)
        return palabras

    def getPalabrasNombreContains(self, nombre, order=(False, "")):
        palabras = Palabra.objects.filter(nombre__icontains=nombre)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasPorLetra(self, letras, order=(False, "")):
        palabras = Palabra.objects.all()
        qset = []
        for letra in letras:
            qset.append(
                Q(nombre__icontains=letra)
            )
        palabras = palabras.filter(reduce(operator.or_, qset))

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasEmpezarLetra(self, letra, order=(False, "")):
        palabras = Palabra.objects.filter(nombre__istartswith=letra)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasTerminarLetra(self, letra, order=(False, "")):
        palabras = Palabra.objects.filter(nombre__iendswith=letra)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasNumeroLetras(self, numero, order=(False, "")):
        # Frases.objects.filter(frase__size = numero)
        palabras = []
        if (order[0]):
            palabras = Palabra.objects.raw(
                "SELECT id, nombre FROM contenido_idioma.Palabra WHERE LENGTH(nombre) = " + str(numero) + " ORDER BY " +
                order[1] + "")
        else:
            palabras = Palabra.objects.raw(
                "SELECT id, nombre FROM contenido_idioma.Palabra WHERE LENGTH(nombre) = " + str(numero) + "")
        return palabras

    def getPalabrasLimit(self, limite, order=(False, "")):
        palabras = Palabra.objects.all()[:limite]
        if order[0]:
            palabras = palabras.order_by(order[1])
        return palabras

    def getPalabrasExectId(self, id, order=(False, "")):
        palabras = Palabra.objects.exclude(id__exact=id)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasExectNombre(self, nombre, order=(False, "")):
        palabras = Palabra.objects.exclude(nombre__exact=nombre)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasExectPalabra(self, palabra, order=(False, "")):
        palabras = []
        if (isinstance(palabra, Palabra)):
            palabras = Palabra.objects.exclude(pk=palabra.id)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras


    def getPalabrasExectLetra(self, letras, order=(False, "")):
        palabras = Palabra.objects.all()
        qset = []
        for letra in letras:
            qset.append(
                Q(nombre__contains=letra)
            )

        palabras = palabras.exclude(reduce(operator.or_, qset))

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasExectEmpezarLetra(self, letra, order=(False, "")):
        palabras = Palabra.objects.exclude(nombre__startswith=letra)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getPalabrasExectTerminarLetra(self, letra, order=(False, "")):
        palabras = Palabra.objects.exclude(nombre__endswith=letra)

        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras


    def getPalabrasExectList(self, lista, order=(False, "")):
        palabras = Palabra.objects.all()
        qset = []
        for palabra in lista:
            qset.append(
                Q(nombre__exact=palabra)
            )

        palabras = palabras.exclude(reduce(operator.or_, qset))
        if (order[0]):
            palabras = palabras.order_by(order[1])

        return palabras

    def getFrases(self, order=(False, "")):
        frases = Frase.objects.all()
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases

    def getFrasesAleatoria(self, limite=0, order=(False, "")):
        count = Frase.objects.all().count()

        if (not (limite == None)):
            if (count >= limite):
                slice = random.random() * (count - limite)
                frases = Frase.objects.all()[slice: slice + limite]
            else:
                frases = Frase.objects.all()
        else:
            frases = Frase.objects.all()

        return frases

    def getFrasesPalabraId(self, id):
        frase = []
        return frase

    def getFrasesExectPalabra(self, id):
        frases = []
        return frases


    def getFrasesPalabraNombre(self, nombre, order=(False, "")):
        frases = Frase.objects.filter(clausula__icontains=nombre)
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases

    def getFrasesExectPalabraNombre(self, nombre, order=(False, "")):
        frases = Frase.objects.exclude(clausula__icontains=nombre)
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases

    def getFrasesExectPalabraId(self, id):
        frases = []
        return frases


    def getFrasesExectPalabra(self, palabra, order=(False, "")):
        frases = []
        return frases


    def getFrasesContenga(self, algo, order=(False, "")):
        frases = Frase.objects.filter(clausula__icontains=algo)

        if order[0]:
            frases = frases.order_by(order[1])

        return frases



    def getFrasesEmpezarCon(self, algo, order=(False, "")):
        frases = Frase.objects.filter(clausula__istartswith=algo)

        if (order[0]):
            frases = frases.order_by(order[1])

        return frases

    def getFrasesTerminarCon(self, algo, order=(False, "")):
        frases = Frase.objects.filter(clausula__iendswith=algo)

        if (order[0]):
            frases = frases.order_by(order[1])

        return frases

    def getFrasesLetras(self, letras, order=(False, "")):
        frases = Frase.objects.all()
        qset = []
        for letra in letras:
            if (len(letra) == 1):
                qset.append(
                    Q(clausula__icontains=letra)
                )

        frases = frases.filter(reduce(operator.or_, qset))
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases


    def getFrasesExectLetras(self, letras, order=(False, "")):
        frases = Frase.objects.all()
        qset = []
        for letra in letras:
            if (len(letra) == 1):
                qset.append(
                    Q(clausula__icontains=letra)
                )
        frases = frases.exclude(reduce(operator.or_, qset))
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases


    def getFrasesPalabras(self, palabras, order=(False, "")):
        frases = Frase.objects.all()
        qset = []
        for palabra in palabras:
            if (isinstance(palabra, Palabra)):
                qset.append(
                    Q(clausula__icontains=palabra.nombre)
                )
            elif (isinstance(palabra, str)):
                qset.append(
                    Q(clausula__icontains=palabra)
                )
        frases = frases.filter(reduce(operator.or_, qset))
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases


    def getFrasesExectPalabras(self, palabras, order=(False, "")):
        frases = Frase.objects.all()
        qset = []
        for palabra in palabras:
            if (isinstance(palabra, Palabra)):
                qset.append(
                    Q(clausula__icontains=palabra.nombre)
                )
            elif (isinstance(palabra, str)):
                qset.append(
                    Q(clausula__icontains=palabra)
                )
        frases = frases.exclude(reduce(operator.or_, qset))
        if (order[0]):
            frases = frases.order_by(order[1])
        return frases


    def getFrasesNumeroPalabras(self, numero, order=(False, "")):
        frases = []

        if (order[0]):
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM contenido_idioma.Frase WHERE wordcount(clausula,' '," + str(
                    numero) + ") ORDER BY " + order[1] + "")  # Frases.objects.filter(frase__size = numero)
        else:
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM contenido_idioma.Frase WHERE wordcount(clausula,' '," + str(
                    numero) + ")")  # Frases.objects.filter(frase__size = numero)
        return frases

    def getFrasesExectNumeroPalabras(self, numero, order=(False, "")):

        if order[0]:
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM contenido_idioma.Frase WHERE not(wordcount(clausula,' '," + str(
                    numero) + ")) ORDER BY " + order[1] + "")  # Frases.objects.filter(frase__size = numero)
        else:
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM contenido_idioma.Frase WHERE not(wordcount(clausula,' '," + str(
                    numero) + "))")
        return frases


    def getFrasesNumeroLetras(self, numero, order=(False, "")):
        frases = []
        if order[0]:
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM Frase WHERE LENGTH(REPLACE(Frase,' ', '')) = " + str(numero) + " ORDER BY " +
                order[1] + "")
        else:
            frases = Frase.objects.raw(
                "SELECT id, clausula FROM Frase WHERE LENGTH(REPLACE(Frase,' ', '')) = " + str(numero) + "")
        return frases


    def getEtiquetas(self, order=(False, "")):
            if (order[0]):
                etiquetas = Etiqueta.objects.all().order_by(order[1])
            else:
                etiquetas = Etiqueta.objects.all()
            return etiquetas




    def getEtiquetasPublicOwner(self,dueno = None, tipo = None):
        etiqueta = ""

        if isinstance(dueno, int) or isinstance(dueno, unicode):
            if (tipo == 'institucion'):
                dueno = get_or_none(Institucion,id = dueno)
            elif (tipo == 'grupo'):
                dueno = get_or_none(Grupo,id = dueno)
            elif (tipo == 'usuario'):
                dueno = get_or_none(Usuario,id = dueno)

        if isinstance(dueno, Institucion):
            etiqueta = str(dueno.id)+":i"
        elif isinstance(dueno, Grupo):
            etiqueta = str(dueno.id)+":g"
        elif isinstance(dueno, Usuario):
            etiqueta = str(dueno.id)+":u"
        elif isinstance(dueno, str):
            etiqueta = dueno


        tagOwner = get_or_none(Etiqueta,nombre__exact = etiqueta)
        idEstado = get_or_none(Estado,nombre__exact = "publico").id  if get_or_none(Estado,nombre__exact = "publico") != None else None
        etiquetasPerteneciente = UsuarioDuenoEtiqueta.objects.filter(etiqueta_id = tagOwner.id) if tagOwner != None else None
        etiquetas = []
        if tagOwner != None and  etiquetasPerteneciente != None:
            query = (Q(estado_id = idEstado) |
                     Q(id__in = etiquetasPerteneciente.values('etiqueta_id1')))
            etiquetas = Etiqueta.objects.filter(query)
        return etiquetas




    def getPalabrasEtiqueta(self, etiqueta = None,  order=(False, "") , estado = None):
        query = []
        if(etiqueta != None):
            if isinstance(etiqueta, Etiqueta):
                query.append(Q(etiqueta__iexact=etiqueta.id))
            else:
                etiquetaExacta = None
                if isinstance(etiqueta, str):
                    etiquetaExacta = Etiqueta.objects.filter(nombre__iexact = etiqueta)[:1]
                elif isinstance(etiqueta, int):
                    etiquetaExacta = Etiqueta.objects.filter(id__exact = etiqueta)[:1]
                query.append(Q(etiqueta__in = etiquetaExacta))#Q(etiqueta__exact=etiquetaExacta[0].id))
        if estado != None:
            if isinstance(estado, Estado):
                query.append(Q(estado__iexact=estado.id))
            else:
                estadoExacta = None
                if isinstance(estado, str):
                    estadoExacta = Estado.objects.filter(nombre__iexact = estado)[:1]
                elif isinstance(estado, int):
                    estadoExacta = Estado.objects.filter(id__exact = estado)[:1]
                query.append(Q(estado__in = estadoExacta))#Q(estado__exact=estadoExacta[0].id))

        palabraEtiqueta = PalabraTieneEtiqueta.objects.filter(reduce(operator.and_, query))

        palabras = Palabra.objects.filter(id__in = palabraEtiqueta.values('palabra'))

        if (order[0]):
            palabras = palabras.order_by(order[1])
        return palabras