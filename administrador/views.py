# Create your views here.
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Registro
#from .import RegistroForm
from django.views.generic import DetailView 
from administrador.forms import RegistroForm

# Create your views here.

def index(request) :
    registros = Registro.objects.all().order_by('-id')
    return render(
        request , 'index.html' , 
        {    
            'message':'Welcome',
            'title':'Taks',
            'registros' : registros,
        }
    )

#def detalles(request , id) :
 #   registro = get_object_or_404(Registro , pk = id) 
#
 #   return render(
  #      request , 'detalles.html' ,
   #     {
    #        'registro ' : registro 
     #   }
    #)
    
    
#clase django para obtener los detalles de los datos
class RegistroDetalle(DetailView): 
    model = Registro 

def crear(request) :
    if request.method == "POST" :
        registro_form = RegistroForm(request.POST)
        if registro_form.is_valid() :
            registro_form.save()
            return redirect('index')
    else :
        registro_form = RegistroForm()

    return render(
        request , 'crear.html' ,
        {
            'registro_form' : registro_form
        }
    )

    

def editar(request , id) :
    registro  = get_object_or_404(Registro , pk = id)

    if request.method == "POST" :
        registro_form = RegistroForm(request.POST , instance = registro ) 
        if registro_form.is_valid() :
            registro_form.save()
            return redirect('index')
    else :
        registro_form = RegistroForm(instance = registro )

    return render(
        request , 'editar.html' ,
        {
            'registro_form' : registro_form
        }
    )

def eliminar(request , id) :
    registro  = get_object_or_404(Registro , pk = id)

    if registro  :
        registro.delete()

    return redirect('index')
