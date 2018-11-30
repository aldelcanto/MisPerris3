from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import redirect
#Importamos los modelos de los perros
from .models import Perros_Rescatados
#Importamos el Formulario 
from .forms import Perro_RescatadoForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm

from django.http import HttpResponse
from django.core import serializers
import json




# Create your views here.
#Devolver a la pagina de inicio
def inicio(request):
	# Se van agregar los post a la platilla.html
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/inicio.html', )

def base_layout(request):
	template='perris/base.html'
	return render(request,template)

def login(request):
    return render(request, 'registration/login.html', {})

def perros_disponibles(request):
# 	#Mostrar los perros disponibles 
# 	# Se van agregar los post a la platilla.html
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/perros_disponibles.html', {'perros': perros})


def administrador_inicio(request):
    perros = Perros_Rescatados.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'perris/adm.inicio.html', {'perros': perros})


#Vista del Agregar un nuevo post de perro rescatadoo
def new_post_perro(request):
    form = Perro_RescatadoForm()
    return render(request, 'perris/adm.perro_post_edit.html', {'form': form})



#Guardar los datos del Formulario del Perro rescatado en la BD 
def new_post_perro(request):
   if request.method == "POST":
       form = Perro_RescatadoForm(request.POST or None , request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('adm.inicio')
   else:
       form = Perro_RescatadoForm()
   return render(request, 'perris/adm.perro_post_edit.html', {'form': form})

#Ver mas detalles del Post Perro
#Detalle del Post
def detail_post_perro(request, pk):
    perros = get_object_or_404(Perros_Rescatados, pk=pk)
    return render(request, 'perris/adm.perro_post_detail.html', {'perro': perros})

#Modificar el POST de Perros y guardarlo
def edit_post_perro(request, pk):
    post = get_object_or_404(Perros_Rescatados, pk=pk)
    if request.method == "POST":
        form = Perro_RescatadoForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail_post_perro', pk=post.pk)
    else:
        form = Perro_RescatadoForm(instance=post)
    return render(request, 'perris/adm.perro_post_edit.html', {'form': form})

#Eliminar el post del perro
def delete_post_perro (request , pk):
    perros= Perros_Rescatados.objects.get(pk=pk)
    if request.method =="POST":
        perros.delete()
        return redirect ('/')
    return render(request, 'perris/adm.perro_post_delete.html', {'perro': perros})

def form(request):
    return render(request, 'registration/form.html',{})

def register(request):
    #guardamos el formulario para ser enviado al
    #template
    variables = {
        'form':CustomCreationForm
    }

    if request.POST:
        #le pasamos todos los campos que vienen
        #desde el navegador al formulario
        form = CustomCreationForm(request.POST)

        if form.is_valid():
            #el formulario se encarga de guardar
            #los datos en la BBDD
            form.save()
            variables['mensaje'] = "Usuario creado"
        else:
            variables['mensaje'] = "No se ha registrado el usuario"
            variables['form'] = form

    return render(request, 'perris/register.html', variables)

