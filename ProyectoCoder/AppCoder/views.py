from django.shortcuts import render
from django.http import HttpResponse 
from AppCoder.models import Familia
from django.template import loader
from django.template import Template, Context

# Create your views here.

def familia(request):
    
    familia1 = Familia(nombre = "Lucia" , edad = 49, fecha ="1973-04-26")
    familia1.save()
    
    
    familia2 = Familia( nombre = "Juan Carlos" , edad = 51, fecha ="1970-12-21")
    familia2.save()
    
    
    familia3 = Familia( nombre = "Leonel" , edad = 29, fecha ="1992-09-14")
    familia3.save()
    
    
    familia4 = Familia( nombre = "Mia" , edad = 15, fecha ="2006-07-23")
    familia4.save()
    
    
    familia5 = Familia(nombre = "Daiana" , edad = 25, fecha ="1996-07-29")
    familia5.save()
    
    
    familia6 = Familia( nombre = "Enzo" , edad = 7, fecha ="2015-02-06")
    familia6.save()
     
    
    familia7 = Familia( nombre = "Mateo" , edad = 1, fecha ="2021-05-14")
    familia7.save()
    

    familiaXD = [familia1, familia2, familia3, familia4, familia5, familia6, familia7]

    plantilla = loader.get_template("template.html")
    documento = plantilla.render({"familia":familiaXD})
    
    return HttpResponse(documento)

    
    