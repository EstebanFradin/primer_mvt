from django.http import HttpResponse
from django.shortcuts import render 
from datetime import date
from AppFamily.models import familiar1



def familiares(request):     
    padre = familiar1(nombre='Alejandro', apellido='Fradin', numero=2613066074, nacimiento= date(1970,11,12))     
    padre.save()     
    madre = familiar1(nombre='Flavia',apellido='Molina', numero=2615559423,  nacimiento= date(1977,3,23))    
    madre.save()     
    hermanastro = familiar1(nombre='Leandro',apellido='Bevilacqua', numero=2613290092, nacimiento= date(2005,7,24))     
    hermanastro.save()     
    return render(request, 'aviso.html')  
    
def familiares_base(request):      
    familiar = familiar1.objects.all()      
    contexto = {'familiares_base':familiar}      
    return render(request, 'plantilla.html', contexto)




