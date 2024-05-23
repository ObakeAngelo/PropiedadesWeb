
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import listar_propiedades, crear_propiedad, actualizar_propiedad, eliminar_propiedad
urlpatterns = [
    path('', views.home, name="home"),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/',views.registro, name='registro'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),

     path('mostrar/', views.listar_propiedades, name='listar'),
    path('mostrar/crear/', views.crear_propiedad, name='crear'),
    path('mostrar/actualizar/<int:pk>/', views.actualizar_propiedad, name='actualizar'),
    path('mostrar/eliminar/<int:pk>/', views.eliminar_propiedad, name='eliminar')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
