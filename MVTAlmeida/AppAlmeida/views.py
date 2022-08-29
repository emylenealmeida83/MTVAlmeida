from pipes import Template
from xml.dom.expatbuilder import DOCUMENT_NODE
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.http import HttpResponse
from .models import familiar
from django.template import context, Template

def familiar(request):
    familiar1= familiar(nombre="Julio Almeida", edad= 62, fecha_nacimiento= "1959/04/25")
    familiar2= familiar(nombre="Stephanie Almeida", edad= 28, fecha_nacimiento= "1993/11/19") 
    familiar3= familiar(nombre="Bianca Almeida", edad= 8, fecha_nacimiento= "2013/09/07")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    documento= f"nombre: {familiar1.nombre} edad:{familiar1.edad} fecha de nacimiento: {familiar1.fecha_nacimiento}"
    return HttpResponse (documento)

def html(request):
    miarchivo= open("MVTAlmeida/MVTAlmeida/template.html")
    contenido=miarchivo.read()
    miarchivo.close()
    plantilla=Template(contenido)
    contexto=context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
