from django import forms
#Importamos el Modelo de Peros_Rescatados
from .models import Perros_Rescatados
#extenderemos el formulario de creacion de usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#traeremos el modelo de User
from django.contrib.auth.models import User


#Crear el formulario de Perro Rescatado 

class Perro_RescatadoForm(forms.ModelForm):
	class Meta:
		model=Perros_Rescatados
		fields=('fotografia_perro','nombre_perro' , 'raza_predominante' , 'descripcion','estado', )	






class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        #le decimos el modelo de BBDD al que esta asociado este
        #formulario
        model = User
        #le decimos a django en que orden aparecerán los campos
        #en el template
        fields = ('username',
        'first_name',
         'last_name',
         'email',
         'password1',
         'password2')
         