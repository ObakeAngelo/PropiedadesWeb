from django.shortcuts import render
from .forms import ActualizarPropiedadForm, CrearPropiedadForm, frmRegistro, frmLogin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from django.http import FileResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Propiedad
from django.contrib.auth.decorators import login_required
from django.views import View

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


@login_required
def listar_propiedades(request):
    propiedades = Propiedad.objects.all().order_by('-id')
    contexto = {}
    form = CrearPropiedadForm()

    default_page = 1
    page = request.GET.get('page', default_page)
    query = request.GET.get('q')

    if query:
        propiedades = propiedades.filter(
            Q(numero_rol__icontains=query) |
            Q(tipo_propiedad__icontains=query) |
            Q(tipo_operacion__icontains=query) |
            Q(metros_cuadrados__icontains=query) |
            Q(precio_tasacion__icontains=query)
        )

    items_per_page = 5
    paginator = Paginator(propiedades, items_per_page)

    try:
        propiedades = paginator.page(page)
    except PageNotAnInteger:
        propiedades = paginator.page(default_page)
    except EmptyPage:
        propiedades = paginator.page(paginator.num_pages)

    contexto["propiedades"] = propiedades
    contexto["form"] = form
    return render(request, 'propiedad/mostrar.html', contexto)


def crear_propiedad(request):
    if request.method == 'POST':
        form = CrearPropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Propiedad agregada correctamente'})
    else:
        form = CrearPropiedadForm()
    return render(request, 'propiedad/mostrar.html', {'form': form})


def actualizar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = ActualizarPropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Propiedad actualizada correctamente'})
    return JsonResponse({'error': 'Formulario no válido'})
    


def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        propiedad.delete()
        return JsonResponse({'message': 'Propiedad eliminada correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
