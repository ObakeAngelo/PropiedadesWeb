from django import forms
from .models import EmpresaCorredora, Propiedad
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Field, ButtonHolder


class frmRegistro(UserCreationForm):
    class Meta:
        model = EmpresaCorredora
        fields = ['rut_empresa','username', 'email', 'telefono', 'password1', 'password2', 'razon_social', 'giro']
        
        
class frmLogin(AuthenticationForm):
    class Meta:
        model = EmpresaCorredora 
        fields = ['username', 'password'] 


class CrearPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'numero_rol', 'tipo_propiedad', 'tipo_operacion', 'titulo', 'estado',
            'descripcion_propiedad', 'metros_cuadrados', 'nro_habitaciones', 'nro_bannos',
            'precio_tasacion', 'direccion_propiedad', 'rut_empresa'
        ]

   

        




class ActualizarPropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'numero_rol', 'tipo_propiedad', 'tipo_operacion', 'estado',
            'descripcion_propiedad', 'metros_cuadrados', 'nro_habitaciones', 'nro_bannos',
            'precio_tasacion', 'direccion_propiedad', 'rut_empresa'
        ]

        

    