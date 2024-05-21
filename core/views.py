from django.shortcuts import render
from .forms import ActualizarPropiedadForm, CrearPropiedadForm, frmRegistro, frmLogin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from django.http import FileResponse
from .models import Propiedad
# Create your views here.


from django.urls import reverse
def home(request):
    return render(request, 'core/home.html')



def registro(request):
    if request.method == 'POST':
        form = frmRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            user.save()
            messages.success(request,"Cuenta creada!")
            return redirect('home')  # Redirigir a la página de inicio después del registro
    else:
        form = frmRegistro()
    
    contexto = {
        'form': form,
    }
        
    return render(request, 'registration/registro.html', contexto)



def iniciar_sesion(request):
    if request.method == 'POST':
        form = frmLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
    else:
        form = frmLogin()
    
    return render(request, 'registration/iniciar_sesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')

class ListarPropiedad(ListView): 
    model = Propiedad
    template_name = 'propiedad/mostrar.html'

class DetallePropiedad(DetailView): 
    model = Propiedad
    template_name = 'propiedad/detalle.html' # Llamamos a la clase 'Jugos' que se encuentra en nuestro archivo 'models.py'



class CrearPropiedad(SuccessMessageMixin, CreateView): 
    model = Propiedad # Llamamos a la clase 'Propiedad' que se encuentra en nuestro archivo 'models.py'
    form_class = CrearPropiedadForm # Definimos nuestro formulario con el nombre de la clase o modelo 'Propiedad'
    # Le decimos a Django que muestre todos los campos de la tabla 'Propiedad' de nuestra Base de Datos 
    template_name = 'propiedad/agregar.html'
    success_message = 'Propiedad Ingresada Correctamente !' # Mostramos este Mensaje luego de Crear una propiedad
    def get_success_url(self):        
        return reverse('mostrar') # Redireccionamos a la vista principal 'leer'
    def form_valid(self, form):
        messages.success(self.request, "Propiedad creada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al crear la propiedad.")
        return super().form_invalid(form)

class ActualizarPropiedad(SuccessMessageMixin, UpdateView): 
    model = Propiedad # Llamamos a la clase 'Propiedad' que se encuentra en nuestro archivo 'models.py' 
    form_class = ActualizarPropiedadForm # Definimos nuestro formulario con el nombre de la clase o modelo 'Propiedad' 
   # Le decimos a Django que muestre todos los campos de la tabla 'Propiedad' de nuestra Base de Datos 
    success_message = 'Propiedad Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar una propiedad 
    template_name = 'propiedad/actualizar.html'
    # Redireccionamos a la página principal luego de actualizar una propiedad 
    def get_success_url(self):               
        return reverse('mostrar') # Redireccionamos a la vista principal 'leer'
 

class EliminarPropiedad(SuccessMessageMixin, DeleteView): 
    model = Propiedad 
    form = Propiedad
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar una propiedad
    def get_success_url(self): 
        success_message = 'Propiedad Eliminada Correctamente !' # Mostramos este Mensaje luego de eliminar
        messages.success (self.request, (success_message))       
        return reverse('mostrar') # Redireccionamos a la vista principal 'leer'


def descargar_pdf(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    response = FileResponse(propiedad.titulo.open('rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{propiedad.titulo.name}"'
    return response
