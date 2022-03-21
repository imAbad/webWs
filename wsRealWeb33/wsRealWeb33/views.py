# Importamos las librerias
# Request: para realizar peticiones
# HttpResponse: para enviar la respuesta usando el protocolo HTTP.

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from django.template.loader import get_template
import datetime
from Aplicaciones.Propiedades.models import propiedades

# Definimos una vista

"""
def bienvenida(request):
    return HttpResponse("Bienvenido al sitio Ws Real")


def inicio(request):
    return HttpResponse("<p style='color: red;'>Bienvenidos al inicio</p>")


def pruebaHtml(request, nombre, edad):
    contenido =
#    <html>
 #   <body>
  #  <p>Nombre: %s / Edad: %s </p>
   # </body>
    #</html>
    % (nombre, edad)
    return HttpResponse(contenido)

# Vista para llamar a una plantilla externa


def plantillaPrueba(request):
    # Abrimos el documento que contiene a la plantilla
    plantillaExterna = open("D:/documentosPersonales/web/2022/djangoProjects/wsWebDjango/wsRealWeb33/wsRealWeb33/templates/plantillaPrueba.html")

    # Cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    # Cerramos el documento
    plantillaExterna.close()

    # Creamos el contexto que nos permite pasar parametros
    contexto = Context()
    # Reenderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)


#Hacemos una vista para plantilla trandicional
def plantillaParametros(request):
    # Creamos distintos tipos de parametros a mostrar
    nombre = "AbadBond" # Variables primitivas 
    fechaActual = datetime.datetime.now() #Variable con información de fecha actual
    lenguajes = ["Python", "Java", "Javascript", "C#"] # Lista con información
    plantillaExterna = open("D:/documentosPersonales/web/2022/djangoProjects/wsWebDjango/wsRealWeb33/wsRealWeb33/templates/plantillaParametros.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context({"nombreApodo": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    documento = template.render(contexto)
    return HttpResponse(documento)

# Hacemos una vista para cargar una plantilla con un loader
def plantillaCargador(request):
    # Creamos distintos tipos de parametros a mostrar
    nombre = "AbadBond" # Variables primitivas 
    fechaActual = datetime.datetime.now() #Variable con información de fecha actual
    lenguajes = ["C++", "Arduino" ,"Python", "Java", "Javascript", "C#"] # Lista con información
    # Especificamos la carpeta donde se encuentran las plantilla 
    #Creamos una variable para asignar la plantilla
    plantillaExterna =loader.get_template("plantillaParametros.html")
    #Descomentar esta linea si vamos a mostrar multiples plantillas
    #plantillaExterna =get_template("plantillaParametros.html")
    # Renderizar el documento
    documento = plantillaExterna.render({"nombreApodo": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)

#Hacemos una vista para cargar una plantilla con un shorcut
def plantillaShorcut(request):
    # Creamos distintos tipos de parametros a mostrar
    nombre = "AbadBond" # Variables primitivas 
    fechaActual = datetime.datetime.now() #Variable con información de fecha actual
    lenguajes = ["PHP", "Cobol", "C++", "Arduino" ,"Python", "Java", "Javascript", "C#"] # Lista con información
    return render(request, "plantillaParametros.html", {"nombreApodo": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
"""

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html")

def acapulcoGolden(request):
    return render(request, "acapulcoGolden.html")

def agents(request):
    return render(request, "agents-grid.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render (request, "services.html")

def property(request):
    idPropiedad = propiedades.id
    nombre = propiedades.nombrePropiedad
    return render(request, "property-single.html", {"id": idPropiedad, "nombre": nombre})